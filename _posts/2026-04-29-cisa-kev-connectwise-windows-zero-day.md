---
title: "CISA Adds Actively Exploited ConnectWise ScreenConnect and Windows Flaws to KEV"
date: 2026-04-29 08:46:00 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, cve, microsoft]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/cisa-adds-actively-exploited.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-windows-flaw-exploited-in-zero-day-attacks/
---

CISA added two actively exploited vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog: CVE-2024-1708, a path traversal flaw in ConnectWise ScreenConnect (CVSS 8.4), and a Windows vulnerability confirmed under zero-day exploitation in the wild. Federal civilian agencies are required to remediate both under mandatory patching timelines.

CVE-2024-1708 in ConnectWise ScreenConnect allows path traversal that can lead to code execution and is already under active exploitation. The Windows zero-day has been observed in attacks targeting federal systems. Organizations running ConnectWise ScreenConnect or unpatched Windows deployments should treat these as emergency patches regardless of federal mandate status.
