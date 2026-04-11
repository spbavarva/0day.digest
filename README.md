# 0day.digest

`0day.digest` is a dark, newsfeed-style Jekyll site for tracking AI launches, cybersecurity incidents, supply-chain attacks, CVEs, and longer-form threat research.

It is built on top of the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme, but the UI, navigation, layouts, pagination, and side panels are heavily customized for a faster “signal feed” reading experience instead of a traditional blog.

Live base URL: [https://spbavarva.github.io/0day.digest/](https://spbavarva.github.io/0day.digest/)

## What the Site Contains

- `Daily Signal`
  A paginated feed of short daily items grouped by date.
- `Must-Know`
  A filtered Daily Signal view for the highest-priority stories.
- `Threat Research`
  Longer analysis posts and deep dives.
- `About`
  Site/about page.

## Current UI Direction

- Dark, high-contrast editorial shell
- Hero-inspired sidebar palette with navy, ember, cream, and muted gold accents
- Custom right-hand panel blocks for `Recently Updated`, `Trending Tags`, and `Tags`
- Custom Daily Signal pagination routed through `/daily-signal/`

## Local Development

From the repo root:

```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --future
```

Open:

```text
http://127.0.0.1:4000/0day.digest/
```

Useful notes:

- `_config.yml` changes require a Jekyll restart.
- Most CSS, include, and post edits can be picked up with a normal refresh.
- Pagination is handled by `jekyll-paginate-v2`.

## Content Model

### Daily Signal posts

Location:

```text
_posts/YYYY-MM-DD-slug.md
```

Typical front matter:

```yaml
---
title: "AWS S3 Files Launches"
date: 2026-04-07 09:30:00 +0000
categories: [Daily Signal]
tags: [aws, cloud-security, devsecops]
severity: medium
must_know: false
sources:
  - name: AWS News Blog
    url: https://aws.amazon.com/blogs/aws/...
---
```

Rules used in the current site:

- Keep body copy short and feed-friendly.
- Include `severity` and `sources` for Daily Signal items.
- Use `must_know: true` sparingly.

### Threat Research posts

Location:

```text
_posts/YYYY-MM-DD-slug.md
```

Typical front matter:

```yaml
---
title: "Dissecting the LiteLLM Kill Chain"
date: 2026-04-08
categories: [Threat Research]
tags: [supply-chain, pypi, llm, malware-analysis]
---
```

These are longer-form posts and do not need `severity` or `must_know`.

## Key Pages and Routes

- `/` redirects into the feed
- `/daily-signal/` is the main paginated Daily Signal feed
- `/daily-signal/page/:num/` contains older Daily Signal pages
- `/must-know/` shows the filtered high-priority feed
- `/threat-research/` lists analysis posts
- `/tags/<tag>/` contains tag archive pages

## Important Project Files

### Site configuration

- [_config.yml](_config.yml)

### Layouts

- [_layouts/daily-signal.html](_layouts/daily-signal.html)
- [_layouts/must-know.html](_layouts/must-know.html)
- [_layouts/threat-research.html](_layouts/threat-research.html)
- [_layouts/post.html](_layouts/post.html)

### Includes

- [_includes/sidebar.html](_includes/sidebar.html)
- [_includes/topbar.html](_includes/topbar.html)
- [_includes/trending-tags.html](_includes/trending-tags.html)
- [_includes/source-links.html](_includes/source-links.html)
- [_includes/date-divider.html](_includes/date-divider.html)
- [_includes/signal-card.html](_includes/signal-card.html)
- [_includes/severity-badge.html](_includes/severity-badge.html)

### Styling

- [assets/css/jekyll-theme-chirpy.scss](assets/css/jekyll-theme-chirpy.scss)

This stylesheet contains the current custom design system, including:

- dark shell colors
- feed typography
- sidebar redesign
- right-panel tag styling
- source/footer overrides
- post metadata styling

## RSS and Draft Workflow

The repo includes an automated RSS-to-draft pipeline for collecting candidate stories and opening reviewable digest PRs.

### Core scripts

- [scripts/fetch_feeds.py](scripts/fetch_feeds.py)
- [scripts/promote_drafts.py](scripts/promote_drafts.py)
- [scripts/apply_selections.py](scripts/apply_selections.py)
- [rss-sources.md](rss-sources.md)
- [CLAUDE.md](CLAUDE.md)

### GitHub Actions

- [.github/workflows/rss-digest.yml](.github/workflows/rss-digest.yml)
  Fetches feeds, runs triage, and opens digest PRs.
- [.github/workflows/publish-drafts.yml](.github/workflows/publish-drafts.yml)
  Promotes selected drafts into `_posts/` after merge.
- [.github/workflows/pages-deploy.yml](.github/workflows/pages-deploy.yml)
  Builds and deploys the site to GitHub Pages.

## Design and Editing Notes

- The site is intentionally not a generic blog.
- Preserve the custom navigation and feed layouts.
- Prefer extending the existing custom stylesheet instead of scattering one-off CSS across many files.
- When editing pagination or routing, verify `/daily-signal/` first because that route is now the main feed entrypoint.

## License

This repository is published under the [MIT License](LICENSE).
