---
title: "Checkmarx Confirms GitHub Repository Data Published on Dark Web After March Supply Chain Attack"
date: 2026-04-27 14:19:00 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html
---

Checkmarx has confirmed that data from its GitHub repository appeared on the dark web, tied to the supply chain attack that occurred on March 23, 2026. Access to the repository was facilitated through the original supply chain attack vector.

Checkmarx provides SAST tooling used by enterprises to audit their own codebases. Exposure of a security vendor's internal repository is high-risk: it may include scanning rule logic, customer integration configurations, or API tokens. Organizations using Checkmarx should treat any tokens or credentials in shared repository configurations as compromised and rotate them promptly.
