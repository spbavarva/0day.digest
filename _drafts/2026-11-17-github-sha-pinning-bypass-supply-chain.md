---
title: "Hackers Found a Way Around GitHub Actions SHA Pinning"
date: 2026-11-17 12:25:06 +0000
categories: [Daily Signal]
tags: [supply-chain, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html
---

SHA pinning — locking a GitHub Action to an exact commit hash instead of a
mutable tag — has become the standard defense against supply-chain attacks
on CI/CD pipelines. Attackers have already found a way around it: in the
March 2026 compromise of Trivy, a widely used open-source security
scanner, attackers planted malicious code disguised as GitHub's official
checkout tool, complete with a convincing label, defeating the assumption
that a pinned SHA guarantees trusted code.

Teams relying on SHA pinning as their sole supply-chain control for GitHub
Actions should add additional verification, such as provenance
attestation, rather than treating pinning alone as sufficient.
