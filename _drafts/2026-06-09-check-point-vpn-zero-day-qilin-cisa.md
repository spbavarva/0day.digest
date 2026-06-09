---
title: "Check Point VPN Auth-Bypass Zero-Day Exploited by Qilin Ransomware, CISA Issues 3-Day Patch Order"
date: 2026-06-09 08:18:39 +0000
categories: [Daily Signal]
tags: [zero-day, ransomware, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/
  - name: SecurityWeek
    url: https://www.securityweek.com/check-point-vpn-zero-day-exploited-in-qilin-ransomware-attacks/
  - name: Dark Reading
    url: https://www.darkreading.com/vulnerabilities-threats/check-point-vpn-flaw-exploited-early-may
---

A critical authentication bypass in Check Point Remote Access VPN and Mobile
Access allows attackers to establish VPN sessions without a valid password,
bypassing authentication entirely. A Qilin ransomware affiliate has been
exploiting the flaw since at least early May, with at least one confirmed
incident attributed to the group. CISA added the vulnerability to its Known
Exploited Vulnerabilities catalog and ordered federal agencies to apply the
patch within three days. Organizations running Check Point Remote Access VPN or
Mobile Access should patch immediately and review VPN logs for unauthorized
connections dating back to early May.
