# Cowork Folder Instructions — AI & Security Signal

## What This Project Is

This is a Jekyll-based daily news journal covering AI and cybersecurity. The site uses the Chirpy theme with heavy UI customization. Posts live in `_posts/`.

## How the Pipeline Works (automated)

The RSS ingestion pipeline runs entirely in GitHub Actions. Your only involvement is reviewing the PR it opens.

```
.github/workflows/rss-digest.yml  (cron 2x daily)
  ├── python3 scripts/fetch_feeds.py --hours 14
  │     → scripts/feed-cache/raw-YYYY-MM-DD-HHMM.{json,md}
  │     → scripts/feed-cache/raw-latest.{json,md}
  ├── claude -p "$(cat scripts/prompts/triage.md)"   (headless, OAuth)
  │     → _drafts/feed-digest-YYYY-MM-DD-AMPM.md   (human review summary)
  │     → _drafts/feed-digest-latest.md             (PR body)
  │     → _drafts/YYYY-MM-DD-<slug>.md × N          (candidate posts)
  └── peter-evans/create-pull-request@v6
        → opens PR "Digest YYYY-MM-DD-HHMM"

You:
  → review the PR on GitHub (mobile or desktop)
  → delete draft files you don't want
  → edit titles/summaries/tags inline if needed
  → merge

.github/workflows/publish-drafts.yml  (on push to main touching _drafts/**)
  ├── python3 scripts/promote_drafts.py
  │     → _drafts/<slug>.md  →  _posts/YYYY-MM-DD-<slug>.md
  │     → deletes _drafts/feed-digest-*.md summary files
  └── git commit + push

.github/workflows/pages-deploy.yml  (existing, unchanged)
  → builds Jekyll, deploys to GitHub Pages
```

## Your Job When Invoked Manually (local dev)

If the user runs `scripts/dry-run.sh` locally or invokes you outside the CI workflow, follow these rules:

### Triage mode

When the user says "triage" or "run a digest" or there's a fresh `scripts/feed-cache/raw-latest.md` to process:

1. Follow `scripts/prompts/triage.md` exactly.
2. Read the latest raw dump, `rss-sources.md`, and this file.
3. Write `_drafts/feed-digest-YYYY-MM-DD-AMPM.md` + `_drafts/feed-digest-latest.md` + one `_drafts/YYYY-MM-DD-<slug>.md` per relevant item.
4. Do not commit or push.

### Edit / override mode

When the user reviews the drafts and says something like "merge items 1, 3, 5" or "publish all except 2":

1. Delete the draft files the user excluded.
2. If they ask for tweaks (severity change, must_know flag, title rewrite), edit the relevant draft file in place.
3. Do not move files into `_posts/` yourself — that's `promote_drafts.py`'s job, which runs in the publish-drafts workflow on merge to main. If the user insists on a local-only publish, run `python3 scripts/promote_drafts.py` and let them commit + push manually.

## Post Format (what `triage.md` must produce)

```yaml
---
title: "Title Here"
date: YYYY-MM-DD HH:MM:SS +0000
categories: [Daily Signal]
tags: [tag1, tag2, tag3]
severity: critical | high | medium | informational
must_know: true | false
sources:
  - name: Source Name
    url: https://example.com
---

Body: 5-10 lines max. Factual, no marketing voice.
```

## Rules

- Never push to git or deploy anything from local runs — CI handles that.
- Keep post bodies SHORT — 5-10 lines max for Daily Signal.
- Use tags from this approved list when possible: `supply-chain`, `ransomware`, `phishing`, `xss`, `sqli`, `rce`, `ssrf`, `privilege-escalation`, `data-breach`, `zero-day`, `ai-launch`, `model-release`, `ai-safety`, `llm`, `vulnerability`, `cve`, `malware`, `cloud-security`, `appsec`, `devsecops`, `anthropic`, `openai`, `google`, `microsoft`, `aws`, `pypi`, `npm`, `github`.
- If a new tag is clearly needed, create it — keep it lowercase and hyphenated.
- `must_know: true` only for severity=critical AND (supply-chain | zero-day under active exploit | source/credential leak | breach > 10k users). When in doubt, leave it false.
- Never fabricate details not present in the feed summary. A shorter post is better than an invented one.
- Never create posts without the user explicitly selecting which items to publish (or the CI workflow generating them as candidate drafts that must go through PR review).

## First-Time Setup (one-time)

1. Generate an OAuth token locally: `claude setup-token`
2. Add it to GitHub repo secrets: `Settings → Secrets and variables → Actions → New repository secret → CLAUDE_CODE_OAUTH_TOKEN`
3. (Optional) create a local `.env` at the repo root with `CLAUDE_CODE_OAUTH_TOKEN=<token>` for `scripts/dry-run.sh`. `.env` is already gitignored.
4. Actions tab → `RSS Digest` → Run workflow to verify end-to-end before cron fires.
