---
title: "GhostAction Supply Chain Campaign Compromises 1,900 GitHub Accounts, Targets 30,000+ Repos"
date: 2026-10-15 08:45:10 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html
---

The GhostAction credential-theft campaign has escalated, now targeting more
than 30,000 repositories across roughly 3,000 GitHub users and organizations.
GitGuardian observed a spike in activity on October 8-9, 2026.

The campaign traces back to about 1,900 compromised GitHub accounts and
attempted to extract 3,174 secrets from public repositories' CI pipelines.

Teams should rotate any CI/CD secrets exposed in affected repositories and
audit GitHub Actions workflows for unauthorized changes.
