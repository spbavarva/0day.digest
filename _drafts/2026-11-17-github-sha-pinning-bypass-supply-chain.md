---
title: "Hackers Found a Way Around GitHub SHA Pinning"
date: 2026-11-17 12:25:06 +0000
categories: [Daily Signal]
tags: [supply-chain, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html
---

SHA pinning — locking GitHub Actions to an exact commit hash — has become
a standard defense against supply chain attacks, but attackers have
already found a way around it. In the March 2026 Trivy hijack, attackers
who compromised the widely used open-source security scanner planted
malicious code disguised as GitHub's official checkout tool, crafted to
survive SHA-pinned workflows.

The technique undermines a control many teams treat as sufficient on its
own. Teams relying on SHA pinning for CI/CD supply chain security should
pair it with action provenance verification rather than treating pinning
alone as a complete defense.
