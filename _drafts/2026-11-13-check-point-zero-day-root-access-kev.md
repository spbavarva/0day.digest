---
title: "Check Point Zero-Day Patched After Root-Access Exploitation Since Late October"
date: 2026-11-13 10:44:22 +0000
categories: [Daily Signal]
tags: [zero-day, privilege-escalation, cve]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/alerts/2026/11/13/cisa-adds-two-known-exploited-vulnerabilities-catalog
---

Check Point Software has released emergency hotfixes for a high-severity flaw
that attackers have been exploiting since late October to gain root
privileges and establish persistence on vulnerable devices. CISA confirmed
active exploitation by adding the flaw, tracked as CVE-2026-123039
(incorrect permission assignment for a critical resource in Check Point
products), to its Known Exploited Vulnerabilities catalog.

Organizations running affected Check Point products should apply the hotfix
immediately and check for indicators of root-level persistence established
before patching.
