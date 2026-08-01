#!/usr/bin/env python3
"""
publish_pr.py — Backlog drain: publish selected drafts from a digest PR branch
straight into _posts/ on the current branch (main), WITHOUT merging the branch.

Used by the backlog-drain flow (.github/workflows/drain-backlog.yml and manual
local runs) to clear the ~85 open digest PRs one commit at a time, with zero
touch to _drafts/ or scripts/feed-cache/ on main (so it can never conflict with
the RSS-digest cron, which only writes those paths on its own PR branches).

Selection rule: publish an item only if its front matter has
severity: critical  OR  must_know: true. Everything else is left unpublished.

For each qualifying draft on <branch>:
  * read `_drafts/<file>` content from the branch (git show <branch>:<path>)
  * parse the `date:` field -> YYYY-MM-DD
  * slug = filename with any leading date stripped
  * write to _posts/<date>-<slug>.md ONLY if that target does not already exist
    (idempotent; protects against re-publishing / cross-digest duplicates)

Prints one line per published post to stdout (so the caller can decide whether
there is anything to commit). Diagnostics go to stderr.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"

DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
DATE_FIELD_RE = re.compile(r"^date:\s*(\S+)", re.MULTILINE)
SEVERITY_RE = re.compile(r"^severity:\s*['\"]?([A-Za-z]+)", re.MULTILINE)
MUST_KNOW_RE = re.compile(r"^must_know:\s*['\"]?(\w+)", re.MULTILINE)


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [git-err] {' '.join(args)}: {r.stderr.strip()}", file=sys.stderr)
        return ""
    return r.stdout


def list_branch_drafts(branch: str) -> list[str]:
    out = git("ls-tree", "--name-only", "-r", branch, "_drafts/")
    return [
        p for p in out.splitlines()
        if p.endswith(".md") and "/feed-digest-" not in p
    ]


def front_matter(body: str) -> str | None:
    m = FRONT_MATTER_RE.match(body)
    return m.group(1) if m else None


def parse_date(fm: str) -> str | None:
    dm = DATE_FIELD_RE.search(fm)
    if not dm:
        return None
    raw = dm.group(1).strip().strip('"').strip("'")
    try:
        return datetime.fromisoformat(raw.replace(" ", "T").split("+")[0]).strftime("%Y-%m-%d")
    except ValueError:
        if len(raw) >= 10 and raw[4] == "-" and raw[7] == "-":
            return raw[:10]
    return None


def qualifies(fm: str) -> bool:
    sev = SEVERITY_RE.search(fm)
    mk = MUST_KNOW_RE.search(fm)
    if sev and sev.group(1).lower() == "critical":
        return True
    if mk and mk.group(1).lower() == "true":
        return True
    return False


def slug_from(name: str) -> str:
    return DATE_PREFIX_RE.sub("", Path(name).stem)


def run(branch: str, dry_run: bool) -> int:
    drafts = list_branch_drafts(branch)
    if not drafts:
        print(f"  no candidate drafts on {branch}", file=sys.stderr)
        return 0

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    published = 0
    for path in drafts:
        body = git("show", f"{branch}:{path}")
        if not body:
            continue
        fm = front_matter(body)
        if fm is None:
            print(f"  [skip] {path} — no front matter", file=sys.stderr)
            continue
        if not qualifies(fm):
            continue  # not critical / must_know
        date = parse_date(fm)
        if not date:
            print(f"  [skip] {path} — unparseable date", file=sys.stderr)
            continue
        target = POSTS_DIR / f"{date}-{slug_from(path)}.md"
        if target.exists():
            print(f"  [dup ] {target.name} already published", file=sys.stderr)
            continue
        print(f"  [PUB ] {target.name}" + (" (dry-run)" if dry_run else ""), file=sys.stderr)
        if not dry_run:
            target.write_text(body)
        # machine-readable line on stdout
        print(str(target.relative_to(ROOT)))
        published += 1

    print(f"\npublish_pr[{branch}]: {published} published"
          + (" (dry run)" if dry_run else ""), file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", required=True, help="e.g. origin/digest/2026-07-28-1818")
    ap.add_argument("--dry-run", action="store_true")
    return run(ap.parse_args().branch, ap.parse_args().dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
