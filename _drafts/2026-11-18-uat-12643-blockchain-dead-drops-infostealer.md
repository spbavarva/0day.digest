---
title: "UAT-12643: North Korea-Aligned Actor Uses Blockchain Dead Drops for Infostealer C2"
date: 2026-11-18 11:00:00 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/uat-12643-suspected-north-korea-aligned-actor-blends-blockchain-resilience-with-targeted-infostealing/
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/the-challenge-of-defending-against-bulletproof-dead-drops-on-public-blockchains/
---

Cisco Talos identified malicious infrastructure tied to a financially
motivated, suspected North Korea-aligned threat group it tracks as
UAT-12643, which combines targeted infostealing with command-and-
control hosted via public blockchain networks.

Talos says this reflects a broader shift in malware C2 design away
from fragile, centralized servers and hardcoded domains toward
decentralized blockchain-based "dead drops" that eliminate single
points of failure and resist conventional takedown efforts.

Because blockchain-hosted C2 data can't be seized or taken offline the
way a domain or server can, defenders should expect this technique to
spread beyond this specific actor.
