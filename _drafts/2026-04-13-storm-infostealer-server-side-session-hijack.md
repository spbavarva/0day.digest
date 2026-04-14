---
title: "Storm Infostealer Uses Server-Side Decryption to Hijack Sessions and Bypass MFA"
date: 2026-04-13 14:05:15 +0000
categories: [Daily Signal]
tags: [malware, data-breach, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/the-silent-storm-new-infostealer-hijacks-sessions-decrypts-server-side/
---

A new infostealer dubbed "Storm" skips local browser decryption entirely, instead
exfiltrating raw encrypted browser data to attacker-controlled servers where decryption
occurs. Varonis research demonstrates how this approach enables session hijacking that
bypasses both passwords and MFA — stolen session tokens are valid regardless of auth factors.

Because no decryption occurs on the victim machine, endpoint tools that detect local
credential-scraping activity miss the theft entirely. Stolen browser sessions grant
immediate authenticated access to any service the victim was logged into. Organizations
should implement session binding controls that tie tokens to device fingerprints or IP
ranges, monitor for anomalous simultaneous session activity from different geolocations,
and consider short session expiry windows for high-value internal applications.
