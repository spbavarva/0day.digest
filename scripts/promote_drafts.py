#!/usr/bin/env python3
"""
promote_drafts.py — Move approved drafts into _posts/.

Called by .github/workflows/publish-drafts.yml on push to main.

Behavior:
- Walks _drafts/*.md
- For each file:
  * If name matches feed-digest-*.md — DELETE (these are review summaries, not posts).
  * Otherwise, parse YAML front matter, read `date` field, move the file to
    _posts/<YYYY-MM-DD>-<slug>.md where YYYY-MM-DD comes from the date field
    and <slug> comes from the original filename (stripping any leading date).
- Idempotent: running twice is a no-op.

Supports --dry-run for local verification.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = ROOT / "_drafts"
POSTS_DIR = ROOT / "_posts"

DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
DATE_FIELD_RE = re.compile(r"^date:\s*(\S+)", re.MULTILINE)


def parse_front_matter_date(body: str) -> str | None:
    m = FRONT_MATTER_RE.match(body)
    if not m:
        return None
    fm = m.group(1)
    dm = DATE_FIELD_RE.search(fm)
    if not dm:
        return None
    raw = dm.group(1).strip().strip('"').strip("'")
    # Accept "2026-04-08" or "2026-04-08 13:00:00 +0000" etc.
    try:
        return datetime.fromisoformat(raw.replace(" ", "T").split("+")[0]).strftime("%Y-%m-%d")
    except ValueError:
        # Last resort: first 10 chars if they look like a date.
        if len(raw) >= 10 and raw[4] == "-" and raw[7] == "-":
            return raw[:10]
    return None


def slug_from_filename(name: str) -> str:
    stem = Path(name).stem
    return DATE_PREFIX_RE.sub("", stem)


def promote(dry_run: bool = False) -> int:
    if not DRAFTS_DIR.exists():
        print(f"No drafts directory at {DRAFTS_DIR}", file=sys.stderr)
        return 0

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    promoted = 0
    deleted = 0
    skipped = 0

    for draft in sorted(DRAFTS_DIR.glob("*.md")):
        if draft.name.startswith("feed-digest-"):
            print(f"  [DEL]  {draft.name}", file=sys.stderr)
            if not dry_run:
                draft.unlink()
            deleted += 1
            continue

        body = draft.read_text()
        date = parse_front_matter_date(body)
        if not date:
            print(f"  [SKIP] {draft.name} — missing or unparseable date field", file=sys.stderr)
            skipped += 1
            continue

        slug = slug_from_filename(draft.name)
        target = POSTS_DIR / f"{date}-{slug}.md"
        if target.exists():
            print(f"  [SKIP] {draft.name} — target {target.name} already exists", file=sys.stderr)
            skipped += 1
            continue

        print(f"  [MOVE] {draft.name} -> _posts/{target.name}", file=sys.stderr)
        if not dry_run:
            target.write_text(body)
            draft.unlink()
        promoted += 1

    print(
        f"\npromote_drafts: {promoted} promoted, {deleted} digest files deleted, {skipped} skipped"
        + (" (dry run)" if dry_run else ""),
        file=sys.stderr,
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Report what would happen without changing files")
    args = ap.parse_args()
    return promote(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
