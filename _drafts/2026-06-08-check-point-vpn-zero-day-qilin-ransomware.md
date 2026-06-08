---
title: "Check Point VPN Zero-Day (CVE-2026-50751) Exploited by Qilin Ransomware Gang"
date: 2026-06-08 14:17:39 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, zero-day, ransomware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/
---

Check Point has confirmed active exploitation of CVE-2026-50751 (CVSS 9.3), a logic flaw in certificate validation affecting Remote Access VPN and Mobile Access deployments configured with the deprecated IKEv1 key exchange. The bug lets an unauthenticated remote attacker bypass password checks entirely. Check Point has now linked the zero-day attacks to the Qilin ransomware gang and released security updates. Organizations running affected VPN gateways should patch immediately and disable IKEv1 where it isn't required.
