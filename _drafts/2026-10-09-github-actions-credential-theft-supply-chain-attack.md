---
title: "Credential-Stealing GitHub Actions Workflow Compromises Maintainer Accounts, Spreads to 340+ Repos"
date: 2026-10-09 19:14:28 +0000
categories: [Daily Signal]
tags: [supply-chain, github, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/credential-stealing-github-actions.html
---

An ongoing credential-theft campaign has compromised two high-profile
open-source maintainer accounts to push a malicious GitHub Actions workflow
into over 340 repositories. Researchers at StepSecurity say the attacker used
the hijacked account of Takashi Kitao, author of the 18,400-star pyxel game
engine, to push the workflow into 27 repositories starting at 13:20 UTC.

The malicious workflow is designed to steal credentials from CI/CD pipelines
that run it. Maintainers who use GitHub Actions should audit recent workflow
file changes in their dependencies and rotate credentials if a compromised
account touched their repository.
