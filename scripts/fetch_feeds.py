#!/usr/bin/env python3
"""
fetch_feeds.py — Pull RSS items for the AI & Security Signal digest.

Reads rss-sources.md, fetches every feed via requests (with timeouts and
retries), parses with feedparser, filters to the last N hours, drops items
already published in previous runs (seen.json), collapses near-duplicate
titles, and writes:

    scripts/feed-cache/raw-YYYY-MM-DD-HHMM.json  (machine)
    scripts/feed-cache/raw-YYYY-MM-DD-HHMM.md    (human / Claude triage)

A symlink-like "latest" pair is also written for downstream consumers:

    scripts/feed-cache/raw-latest.json
    scripts/feed-cache/raw-latest.md

Usage:
    python3 scripts/fetch_feeds.py                # last 14h, default
    python3 scripts/fetch_feeds.py --hours 24     # custom window
    python3 scripts/fetch_feeds.py --validate     # probe feeds only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import feedparser
except ImportError:
    print("ERROR: feedparser not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "rss-sources.md"
CACHE_DIR = ROOT / "scripts" / "feed-cache"
SEEN_FILE = CACHE_DIR / "seen.json"

USER_AGENT = (
    "Mozilla/5.0 (compatible; ai-security-signal/1.0; "
    "+https://spbavarva.github.io/ai-security-signal)"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, */*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
}
REQUEST_TIMEOUT = 15  # seconds
MAX_RETRIES = 2       # total attempts = MAX_RETRIES + 1
SEEN_TTL_DAYS = 30
JACCARD_THRESHOLD = 0.8

# match a bullet line like:  - Name — https://url  (supports — – - :)
FEED_LINE = re.compile(r"^\s*[-*]\s+(?P<name>.+?)\s*[—–\-:]\s*(?P<url>https?://\S+)\s*$")


def parse_sources(path: Path) -> list[tuple[str, str, str]]:
    """Return list of (section, name, url) from rss-sources.md. Stops at Twitter/rules sections."""
    feeds: list[tuple[str, str, str]] = []
    section = "Uncategorized"
    skip_section = False
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            section = line[3:].strip()
            low = section.lower()
            skip_section = (
                "twitter" in low or "manual" in low
                or "relevant" in low or "skippable" in low
            )
            continue
        if line.startswith("### "):
            continue
        if skip_section:
            continue
        m = FEED_LINE.match(line)
        if not m:
            continue
        name = m.group("name").strip()
        url = m.group("url").strip().rstrip(".,")
        if not url.startswith(("http://", "https://")):
            continue
        feeds.append((section, name, url))
    return feeds


def entry_time(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        t = getattr(entry, key, None) or entry.get(key)
        if t:
            try:
                return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
            except Exception:
                pass
    return None


def norm_title(title: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", (title or "").lower())).strip()


def title_tokens(title: str) -> set[str]:
    stop = {"the", "a", "an", "of", "in", "on", "for", "to", "and", "or", "with", "from", "by", "is", "are"}
    toks = {t for t in norm_title(title).split() if len(t) > 2 and t not in stop}
    return toks


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def url_key(url: str) -> str:
    p = urlparse(url)
    return (p.netloc + p.path).rstrip("/")


def url_hash(url: str) -> str:
    return hashlib.sha256(url_key(url).encode("utf-8")).hexdigest()


def load_seen() -> dict[str, str]:
    """Return {url_hash: iso_seen_at}. Expired entries dropped."""
    if not SEEN_FILE.exists():
        return {}
    try:
        data = json.loads(SEEN_FILE.read_text())
    except json.JSONDecodeError:
        return {}
    cutoff = datetime.now(timezone.utc) - timedelta(days=SEEN_TTL_DAYS)
    return {
        h: ts for h, ts in data.items()
        if ts and datetime.fromisoformat(ts.replace("Z", "+00:00")) >= cutoff
    }


def save_seen(seen: dict[str, str]) -> None:
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps(seen, indent=2, sort_keys=True))


def http_get(url: str) -> tuple[int, bytes, str | None]:
    """Return (status_code, body, error). Retries with exponential backoff."""
    last_err = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT, allow_redirects=True)
            if resp.status_code >= 500 and attempt < MAX_RETRIES:
                time.sleep(1.5 ** attempt)
                continue
            return resp.status_code, resp.content, None
        except requests.exceptions.RequestException as e:
            last_err = f"{type(e).__name__}: {e}"
            if attempt < MAX_RETRIES:
                time.sleep(1.5 ** attempt)
                continue
    return 0, b"", last_err


def fetch_feed(section: str, name: str, url: str, cutoff: datetime) -> dict:
    """Return {'status': 'ok'|'empty'|'error', 'items': [...], 'error': str|None}."""
    status, body, err = http_get(url)
    if err:
        return {"status": "error", "items": [], "error": err}
    if status >= 400:
        return {"status": "error", "items": [], "error": f"HTTP {status}"}
    if not body:
        return {"status": "error", "items": [], "error": "empty response body"}

    parsed = feedparser.parse(body)
    if getattr(parsed, "bozo", False) and not parsed.entries:
        bozo_err = getattr(parsed, "bozo_exception", "unknown parse error")
        return {"status": "error", "items": [], "error": f"parse: {bozo_err}"}

    items = []
    for e in parsed.entries:
        ts = entry_time(e)
        if ts is None or ts >= cutoff:
            items.append({
                "section": section,
                "source": name,
                "title": (e.get("title") or "").strip(),
                "url": (e.get("link") or "").strip(),
                "published": ts.isoformat() if ts else None,
                "summary": re.sub(
                    r"<[^>]+>", "",
                    (e.get("summary") or e.get("description") or "")
                ).strip()[:600],
            })

    if not parsed.entries:
        return {"status": "empty", "items": [], "error": None}
    return {"status": "ok", "items": items, "error": None}


def dedupe(items: list[dict], seen: dict[str, str]) -> tuple[list[dict], int, int]:
    """Drop items seen in prior runs, collapse near-dup titles, return (kept, seen_skipped, near_dup_skipped)."""
    seen_skipped = 0
    near_dup_skipped = 0
    stage1: list[dict] = []
    exact_urls: set[str] = set()
    exact_titles: set[str] = set()

    for it in items:
        if not it.get("url"):
            continue
        uhash = url_hash(it["url"])
        if uhash in seen:
            seen_skipped += 1
            continue
        ukey = url_key(it["url"])
        tkey = norm_title(it["title"])
        if ukey in exact_urls:
            continue
        if tkey and tkey in exact_titles:
            continue
        exact_urls.add(ukey)
        if tkey:
            exact_titles.add(tkey)
        stage1.append(it)

    # Near-dup pass: Jaccard over title token sets. Keep first occurrence.
    kept: list[dict] = []
    tokens_kept: list[tuple[set[str], dict]] = []
    for it in stage1:
        toks = title_tokens(it["title"])
        is_dup = False
        for prev_toks, prev in tokens_kept:
            if jaccard(toks, prev_toks) >= JACCARD_THRESHOLD:
                # same story; prefer whichever has the higher-priority section
                is_dup = True
                near_dup_skipped += 1
                break
        if not is_dup:
            tokens_kept.append((toks, it))
            kept.append(it)

    return kept, seen_skipped, near_dup_skipped


# Section priority: lower number = higher priority. Used to sort before dedup.
SECTION_PRIORITY = {
    "Cybersecurity — Primary": 0,
    "Cybersecurity — Research & Threat Intel": 1,
    "AI / Model Launches": 2,
    "Mixed / General Tech Security": 3,
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=14, help="look-back window in hours (default 14)")
    ap.add_argument("--validate", action="store_true", help="probe feeds only; do not emit items")
    ap.add_argument("--out-dir", default=str(CACHE_DIR), help="where to write cache files")
    ap.add_argument("--no-seen", action="store_true", help="ignore seen.json (useful for local testing)")
    args = ap.parse_args()

    feeds = parse_sources(SOURCES_FILE)
    if not feeds:
        print(f"ERROR: no feeds parsed from {SOURCES_FILE}", file=sys.stderr)
        return 2

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    now = datetime.now(timezone.utc)
    results = []
    all_items: list[dict] = []
    ok = empty = err = 0

    print(f"Fetching {len(feeds)} feeds (window: last {args.hours}h)...", file=sys.stderr)
    for section, name, url in feeds:
        r = fetch_feed(section, name, url, cutoff)
        results.append({"section": section, "name": name, "url": url, **r, "items": len(r["items"])})
        if r["status"] == "ok":
            ok += 1
            all_items.extend(r["items"])
            print(f"  [OK]    {name}: {len(r['items'])} items in window", file=sys.stderr)
        elif r["status"] == "empty":
            empty += 1
            print(f"  [EMPTY] {name}", file=sys.stderr)
        else:
            err += 1
            print(f"  [ERR]   {name}: {r['error']}", file=sys.stderr)

    # Sort so that higher-priority sections win near-dup dedup.
    all_items.sort(key=lambda i: (
        SECTION_PRIORITY.get(i.get("section", ""), 99),
        -(datetime.fromisoformat(i["published"]).timestamp() if i.get("published") else 0),
    ))

    seen = {} if args.no_seen else load_seen()
    kept, seen_skipped, near_dup_skipped = dedupe(all_items, seen)

    # Record every kept item into seen.json so next run doesn't re-surface.
    if not args.no_seen and not args.validate:
        stamp_iso = now.isoformat()
        for it in kept:
            seen[url_hash(it["url"])] = stamp_iso
        save_seen(seen)

    # Re-sort kept items by published desc for the human output.
    kept.sort(key=lambda i: i.get("published") or "", reverse=True)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = now.strftime("%Y-%m-%d-%H%M")
    json_path = out_dir / f"raw-{stamp}.json"
    md_path = out_dir / f"raw-{stamp}.md"

    payload = {
        "generated_at": now.isoformat(),
        "window_hours": args.hours,
        "feed_count": len(feeds),
        "feeds_ok": ok,
        "feeds_empty": empty,
        "feeds_error": err,
        "item_count": len(kept),
        "seen_skipped": seen_skipped,
        "near_dup_skipped": near_dup_skipped,
        "feeds": results,
        "items": kept,
    }
    json_path.write_text(json.dumps(payload, indent=2))

    lines = [
        f"# Raw feed pull — {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"- Window: last {args.hours}h",
        f"- Feeds: {len(feeds)} ({ok} ok, {empty} empty, {err} error)",
        f"- Items kept after dedup: {len(kept)} "
        f"(seen-skipped: {seen_skipped}, near-dup-skipped: {near_dup_skipped})",
        "",
        "## Feed health",
        "",
    ]
    for r in results:
        badge = {"ok": "OK", "empty": "EMPTY", "error": "ERR"}[r["status"]]
        extra = f" — {r['error']}" if r.get("error") else ""
        lines.append(f"- [{badge}] {r['name']} ({r['items']} items){extra}")

    if not args.validate:
        lines += ["", "## Items", ""]
        for i, it in enumerate(kept, 1):
            lines.append(f"### {i}. {it['title'] or '(no title)'}")
            lines.append(f"- Section: {it.get('section', 'unknown')}")
            lines.append(f"- Source: {it['source']}")
            lines.append(f"- URL: {it['url']}")
            if it.get("published"):
                lines.append(f"- Published: {it['published']}")
            if it.get("summary"):
                lines.append(f"- Summary: {it['summary']}")
            lines.append("")

    md_path.write_text("\n".join(lines))

    # Maintain a stable "latest" pointer for the triage step.
    latest_json = out_dir / "raw-latest.json"
    latest_md = out_dir / "raw-latest.md"
    latest_json.write_text(json_path.read_text())
    latest_md.write_text(md_path.read_text())

    print(f"\nWrote {json_path}", file=sys.stderr)
    print(f"Wrote {md_path}", file=sys.stderr)
    print(f"Wrote {latest_md} (pointer)", file=sys.stderr)
    print(
        f"\n{len(kept)} items from {ok}/{len(feeds)} healthy feeds "
        f"({seen_skipped} already seen, {near_dup_skipped} near-dup)",
        file=sys.stderr,
    )
    print(str(md_path))  # stdout = path to md, for downstream consumers
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
