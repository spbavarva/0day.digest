---
title: "GlassWorm Developer Supply Chain Botnet Dismantled by Industry Coalition"
date: 2026-05-27 11:48:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, npm, github, devsecops]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html
---

CrowdStrike, Google, and the Shadowserver Foundation simultaneously disrupted
all four C2 channels used by GlassWorm, including infrastructure relying on
Solana blockchain transactions and the BitTorrent DHT network — architecture
specifically designed to resist traditional domain-based takedowns.

GlassWorm has targeted software developers through malicious npm packages and
IDE extensions since at least early 2025. Developers should audit package
histories for GlassWorm-associated packages and check for unauthorized extensions
in their development environments. The C2 disruption removes active command
capability but previously installed implants may remain active.
