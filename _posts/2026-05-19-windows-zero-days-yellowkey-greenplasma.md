---
title: "Windows Zero-Day Barrage: YellowKey, GreenPlasma, and MiniPlasma Disclosed Post-Patch Tuesday"
date: 2026-05-19 21:06:54 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, cve, microsoft]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/windows-zero-day-barrage-continues-after-patch-tuesday
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/microsoft-releases-mitigation-for.html
---

A security researcher has disclosed three additional Windows zero-days — YellowKey, GreenPlasma, and
MiniPlasma — continuing a six-week stream of vulnerabilities targeting Windows security primitives.
YellowKey (CVE-2026-45585, CVSS 6.8) is a BitLocker security feature bypass for which Microsoft has
issued a mitigation; no full patches for GreenPlasma or MiniPlasma have been released.

Administrators should apply the available YellowKey mitigation immediately and monitor Microsoft
security advisories for patches covering the remaining two. Environments relying on BitLocker for
device encryption on laptops or regulated workstations face elevated risk until full remediation is
available.
