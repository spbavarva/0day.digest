---
title: "Chinese APT Exploited BeyondTrust Zero-Day Since August; Patch Now Available"
date: 2026-10-16 06:55:55 +0000
categories: [Daily Signal]
tags: [zero-day, cve, privilege-escalation, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/china-linked-hackers-exploited.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/beyondtrust-patches-zero-day-exploited-in-attacks-since-august/
---

A China-nexus espionage group tracked as Armory Castle (previously UNC5221
or Warp Panda) exploited CVE-2026-102764, a CVSS 9.3 improper-origin-
validation flaw in BeyondTrust Remote Support (formerly Bomgar), as a
zero-day beginning in late August 2026 to take over remote support servers.

BeyondTrust has since released a patch for the flaw, and CISA added
CVE-2026-102764 to its Known Exploited Vulnerabilities catalog based on
evidence of active exploitation.

Organizations running BeyondTrust Remote Support should patch immediately
and review remote support server logs for signs of compromise dating back
to August 2026.
