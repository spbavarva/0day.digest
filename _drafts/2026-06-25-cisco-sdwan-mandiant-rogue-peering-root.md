---
title: "Mandiant: Cisco SD-WAN Zero-Day Exploited via Rogue Peering Two Months Before Patch"
date: 2026-06-25 05:46:54 +0000
categories: [Daily Signal]
tags: [zero-day, privilege-escalation, rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/mandiant-reveals-how-cisco-sd-wan-zero-day-attacks-gained-root-access/
---

Google-owned Mandiant disclosed that CVE-2026-20245, a high-severity flaw
(CVSS 7.8) in Cisco Catalyst SD-WAN, was exploited as a zero-day for roughly
two months before it was publicly disclosed and patched. According to
Mandiant, an unknown threat actor used rogue peering to connect to victims'
SD-WAN devices, then abused the authenticated, local privilege-escalation bug
to execute arbitrary commands and create rogue root accounts. This is the
seventh Cisco SD-WAN vulnerability exploited in 2026. Administrators should
audit SD-WAN device peering configurations and root/admin account lists for
unauthorized entries, not just confirm the patch is applied.
