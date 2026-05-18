---
title: "Triple Supply Chain Strike: npm, PyPI, and Docker Hub Targeted in 48-Hour Window"
date: 2026-05-18 11:23:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, pypi, devsecops, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/developer-workstations-are-now-part-of.html
---

Three coordinated supply chain campaigns struck npm, PyPI, and Docker Hub within a 48-hour window, all sharing the same objective: stealing secrets from developer environments and CI/CD pipelines. Targeted credentials include API keys, cloud credentials, SSH keys, and tokens — the access that signs and deploys trusted software downstream. The simultaneous multi-platform targeting signals a deliberate strategy: compromise the developer's workstation or build environment first, then leverage that access to reach production. Organizations should enforce least-privilege access tokens, audit CI/CD secret exposure, and monitor for unexpected outbound connections from build environments.
