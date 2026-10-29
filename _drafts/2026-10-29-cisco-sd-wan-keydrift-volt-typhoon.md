---
title: "Hackers Exploited Cisco SD-WAN Flaw to Plant KeyDrift Malware, Linked to Volt Typhoon"
date: 2026-10-29 08:24:22 +0000
categories: [Daily Signal]
tags: [malware, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html
  - name: SecurityWeek
    url: https://www.securityweek.com/cisco-sd-wan-zero-day-exploitation-tied-to-volt-typhoons-silent-train-network/
---

Hackers exploited a critical Cisco Catalyst SD-WAN flaw, fixed in
February, to plant custom malware inside systems that control an
organization's SD-WAN network.

The malware, called KeyDrift, is designed to copy the keys that encrypt
traffic between sites for later use. Cisco Talos said on October 28 that
the attacks are historical, and linked the infrastructure to overlap
with Volt Typhoon's "Silent Train" network, separately detailed by
Lumen. Organizations running Cisco Catalyst SD-WAN should confirm the
February patch is applied and review for signs of key compromise.
