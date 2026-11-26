---
title: "North Korea-Linked PolinRider Poisons Over 7,600 GitHub Repositories to Spread Malware"
date: 2026-11-26 15:13:41 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html
---

Threat actors behind the PolinRider campaign, linked to North Korea, have
planted a Python loader across more than 7,600 GitHub repositories.

Researchers at SafeDep say the loader hides inside small utils packages
or conftest.py files, so it executes automatically when Python imports
the module.

Evidence suggests the campaign has been running since as early as
February 2025, making it a long-running, large-scale supply chain
poisoning effort rather than an isolated incident.

Developers pulling dependencies from unfamiliar or low-reputation GitHub
repos should audit for unexpected conftest.py or utils-package content.
