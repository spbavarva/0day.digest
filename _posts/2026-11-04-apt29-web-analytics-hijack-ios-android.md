---
title: "APT29 Hijacks Web Analytics Script to Deliver iOS and Android Exploits"
date: 2026-11-04 14:27:52 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html
---

Russia-linked APT29 is behind a large-scale watering hole campaign targeting
iOS and Android users through compromised websites and fake domains,
according to Sekoia researchers. The campaign involves a supply-chain
compromise of Plerdy SEO Tracker, a Ukrainian web analytics service, with
injected JavaScript collecting browser and device attributes to fingerprint
targets before delivering mobile exploits.

Compromising a third-party analytics script gave the attackers reach across
every site embedding it, rather than requiring them to breach each target
site individually.
