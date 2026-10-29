---
title: "Cisco SD-WAN Zero-Day Exploited to Deploy KeyDrift Malware, Linked to Volt Typhoon"
date: 2026-10-29 18:38:26 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, cve, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/
  - name: SecurityWeek
    url: https://www.securityweek.com/cisco-sd-wan-zero-day-exploitation-tied-to-volt-typhoons-silent-train-network/
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html
---

An APT tracked as UAT-11473 exploited CVE-2026-20127, an authentication-bypass
flaw in Cisco Catalyst SD-WAN Controllers (fixed in February), to deploy a
custom malware framework called KeyDrift. KeyDrift is built to copy and store
the encryption keys that secure inter-site traffic for later use.

Cisco Talos linked the attack infrastructure to Volt Typhoon's "Silent Train"
network, previously detailed by Lumen. The attacks are described as
historical, with no confirmed timeline disclosed. Organizations running
Catalyst SD-WAN Controllers should confirm patch status immediately and
rotate encryption keys if compromise is suspected.
