---
title: "Kimwolf v7 Android Botnet Disguises HTTP/2 DDoS Traffic as Legitimate Browsing"
date: 2026-08-11 19:36:37 +0000
categories: [Daily Signal]
tags: [malware, ddos]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/kimwolf-v7-android-botnet-makes-http2.html
---

Palo Alto Networks Unit 42 identified Kimwolf v7 (aka AISURU), a new
version of an Android and IoT botnet used for distributed denial-of-service
attacks.

The new version adds HTTP/2-based DDoS traffic engineered to blend in with
legitimate browsing traffic, improving both operational resilience and
attack effectiveness.

Defenders relying on simple traffic-pattern heuristics for DDoS detection
should account for this evasion technique.
