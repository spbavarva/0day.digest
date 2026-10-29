---
title: "Cisco Patches Second Actively Exploited ASA/FTD VPN Zero-Day Since August"
date: 2026-10-29 10:44:46 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/
  - name: SecurityWeek
    url: https://www.securityweek.com/attackers-exploit-second-cisco-firewall-vpn-zero-day-since-august/
---

Cisco patched CVE-2026-76418 (CVSS 8.6), a flaw in the Remote Access SSL VPN
service of Secure Firewall ASA and FTD software that lets an unauthenticated,
remote attacker force affected firewalls to reload. Cisco confirmed active
exploitation in the wild.

This is the second Cisco ASA/FTD VPN zero-day exploited since August.
Administrators running ASA/FTD should patch immediately regardless of
whether they've observed reload events.
