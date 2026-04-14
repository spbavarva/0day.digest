---
title: "CISA Adds 6 Known Exploited CVEs: Fortinet FortiClient EMS, Windows, and Adobe"
date: 2026-04-14 05:39:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, zero-day, fortinet, microsoft, adobe]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/cisa-adds-6-known-exploited-flaws-in.html
---

CISA added six vulnerabilities to its Known Exploited Vulnerabilities catalog, all confirmed
exploited in the wild. The most severe is CVE-2026-21643 (CVSS 9.1), an SQL injection flaw in
Fortinet FortiClient EMS that allows unauthenticated remote attackers to execute arbitrary SQL
commands.

The batch also includes Windows privilege escalation and Adobe Acrobat code execution
vulnerabilities. KEV listings carry mandatory remediation deadlines for US federal agencies and
serve as strong guidance for the private sector.

Organizations using Fortinet FortiClient EMS, any Windows version, or Adobe Acrobat should
treat these as priority patches. Unauthenticated SQLi in a widely deployed endpoint management
system is high-value for initial access.
