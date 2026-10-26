---
title: "Gheist Campaign Uses Stolen GitHub Tokens to Exfiltrate Secrets via Actions Logs"
date: 2026-10-26 07:49:46 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html
---

An automated campaign dubbed Gheist is using stolen GitHub tokens to plant
workflows that print a repository's secrets into its GitHub Actions logs,
which attackers then download before deleting the runs.

The attacks have succeeded against private repositories and GitHub
Enterprise environments, according to analysis from cloud security company
Wiz. Organizations should audit Actions logs for unexpected secret exposure
and rotate tokens used in recent workflow runs.
