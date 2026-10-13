---
title: "GitHub Tightens npm Trusted Publishing After Flaw Left 1,500+ Packages Hijackable"
date: 2026-10-13 16:18:18 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html
---

Researchers found that GitHub's npm trusted publishing feature could let
an attacker push new versions of another user's package without stealing
their credentials, due to how unvalidated trusted-publishing
configurations were handled — leaving more than 1,500 packages vulnerable
to hijacking.

GitHub has responded by expiring unvalidated trusted publishing
configurations 48 hours after creation; a configuration becomes exempt
from expiry after its first successful publish. Maintainers using npm
trusted publishing should confirm their configuration completed a
successful publish.
