---
title: "New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions"
date: 2026-07-06 08:50:54 +0000
categories: [Daily Signal]
tags: [malware, vulnerability]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-trojpix-attack-leaks-data-from-air.html
---

Researchers at Shandong University demonstrated TrojPix, a technique that
exfiltrates data from air-gapped machines by subtly modifying on-screen
pixels so the video cable's electromagnetic emissions carry a decodable radio
signal to a nearby receiver. The pixel changes are imperceptible to a person
looking at the screen. TrojPix only works once malware is already running on
the target machine, so it's a post-compromise exfiltration channel rather
than an initial-access technique. It adds to the family of air-gap covert
channels that rely on hardware emissions instead of network connectivity.
