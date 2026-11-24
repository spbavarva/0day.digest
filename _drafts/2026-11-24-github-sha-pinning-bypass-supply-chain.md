---
title: "Attackers Find a Way Around GitHub Actions SHA Pinning"
date: 2026-11-24 12:42:09 +0000
categories: [Daily Signal]
tags: [supply-chain, github, devsecops]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html
---

SHA pinning for GitHub Actions, long considered the standard defense against
software supply chain attacks, can be circumvented. The technique echoes the
March 2026 hijack of the open-source Trivy security scanner, where attackers
planted malicious code disguised as GitHub's official checkout tool, complete
with a legitimate-looking label.

Teams relying solely on SHA pinning to secure CI/CD pipelines should review
additional supply chain controls.
