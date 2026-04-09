#!/usr/bin/env bash
# dry-run.sh — Local end-to-end helper for the RSS → triage pipeline.
#
# Usage:
#   1) Create .env at the repo root with: CLAUDE_CODE_OAUTH_TOKEN=<your-token>
#   2) ./scripts/dry-run.sh             # fetch (14h) + triage
#   3) ./scripts/dry-run.sh 24          # custom hours window
#
# The script will:
#   - source .env (if present) so CLAUDE_CODE_OAUTH_TOKEN is set
#   - run scripts/fetch_feeds.py to populate scripts/feed-cache/raw-latest.md
#   - run `claude -p` in headless mode with the triage prompt
#   - print the resulting _drafts/ file list for quick inspection
#
# It will NOT commit or push anything. It's just fetch + triage for local iteration.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

HOURS="${1:-14}"

if [[ -f .env ]]; then
  # shellcheck disable=SC1091
  set -a; source .env; set +a
fi

if [[ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]]; then
  echo "ERROR: CLAUDE_CODE_OAUTH_TOKEN not set. Put it in .env or export it." >&2
  exit 1
fi

if ! command -v claude >/dev/null 2>&1; then
  echo "ERROR: 'claude' CLI not on PATH. Install: npm i -g @anthropic-ai/claude-code" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found." >&2
  exit 1
fi

echo "==> Fetching feeds (last ${HOURS}h)..."
python3 scripts/fetch_feeds.py --hours "$HOURS" --no-seen

echo ""
echo "==> Running Claude triage (headless)..."
claude -p "$(cat scripts/prompts/triage.md)" \
  --permission-mode acceptEdits \
  --allowed-tools "Read,Write,Glob,Grep"

echo ""
echo "==> Drafts produced:"
ls -la _drafts/ 2>/dev/null || echo "(none)"
