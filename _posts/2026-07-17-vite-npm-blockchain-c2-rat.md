---
title: "Seven Malicious npm Packages Target Vite, Use Blockchain C2 to Deliver RAT"
date: 2026-07-17 18:54:51 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html
---

Researchers at Checkmarx identified seven malicious npm packages targeting
the Vite frontend tooling ecosystem, part of a campaign codenamed
ViteVenom. The campaign expands ChainVeil, a supply chain operation that
uses a four-tier blockchain-based command-and-control infrastructure
spanning multiple chains, including Tron, to deliver a remote access
trojan. Developers using Vite-adjacent tooling should audit recent npm
installs and lockfiles for the flagged packages.
