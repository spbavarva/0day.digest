---
title: "TrickMo Android Banking Trojan Adopts TON Blockchain C2 and SOCKS5 Network Pivoting"
date: 2026-05-12 12:50:00 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html
---

ThreatFabric researchers identified a new TrickMo Android banking trojan variant observed
between January and February 2026, targeting banking and cryptocurrency wallet users in
France, Italy, and Austria. The variant routes command-and-control traffic through The Open
Network (TON), a legitimate decentralized blockchain network, making traffic blocking on
infrastructure level significantly harder than with traditional C2 domains. It also
establishes SOCKS5 proxies on infected devices to create network pivots into victim
environments. The malware dynamically loads a DEX module at runtime to evade static
analysis. Mobile security teams and banking app developers should review device attestation
controls and ensure fraud detection systems account for SOCKS5 relay patterns.
