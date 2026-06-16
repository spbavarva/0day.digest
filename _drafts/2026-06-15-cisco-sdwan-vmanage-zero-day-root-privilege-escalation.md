---
title: "Cisco Patches SD-WAN vManage Zero-Day Exploited for Root Privilege Escalation"
date: 2026-06-15 17:12:42 +0000
categories: [Daily Signal]
tags: [zero-day, privilege-escalation, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/alerts/2026/06/15/cisa-adds-two-known-exploited-vulnerabilities-catalog
---

Cisco has released security updates for a directory/path traversal vulnerability (CVE-2026-20262) in Catalyst SD-WAN Manager (vManage) that attackers exploited in the wild to escalate to root privileges.
CISA added CVE-2026-20262 to its Known Exploited Vulnerabilities catalog based on evidence of active exploitation, requiring federal civilian agencies to remediate under Binding Operational Directive 26-04.
Organizations running Catalyst SD-WAN Manager should apply Cisco's patch immediately and review for signs of unauthorized administrative access.
CISA separately added a second actively exploited flaw, CVE-2026-54420, a UNIX symlink-following vulnerability in the LiteSpeed cPanel plugin, to the same catalog update.
