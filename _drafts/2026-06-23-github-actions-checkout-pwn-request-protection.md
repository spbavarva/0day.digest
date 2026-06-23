---
title: "GitHub Hardens actions/checkout Against Pwn Request Attacks"
date: 2026-06-23 14:22:03 +0000
categories: [Daily Signal]
tags: [supply-chain, github, devsecops]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html
---

GitHub is updating its official actions/checkout GitHub Action to block "pwn
request" attacks, which exploit risky use of the pull_request_target
workflow trigger to run malicious code with the workflow's full privileges.
The hardened version takes effect June 18, 2026. Repository maintainers using
pull_request_target workflows should update to the latest actions/checkout
release and review their workflow permissions.
