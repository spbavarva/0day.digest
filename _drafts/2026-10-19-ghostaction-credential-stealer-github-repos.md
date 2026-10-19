---
title: "GhostAction Attackers Plant Font-Disguised Credential Stealer in 94 GitHub Repos"
date: 2026-10-19 13:05:45 +0000
categories: [Daily Signal]
tags: [supply-chain, github, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/ghostaction-attackers-plant-credential.html
---

The threat actor behind the GhostAction supply chain campaign has expanded
beyond malicious GitHub Actions workflows, now phishing open-source
developers and delivering credential-stealing malware disguised as a font
file, according to research from OpenSourceMalware.

The stealer has been planted across 94 GitHub repositories so far, signaling
the group is actively evolving its tactics in response to prior mitigation
efforts. Maintainers of public repos should review recent commits and
dependencies for unfamiliar font or asset files.
