---
title: "Microsoft Defender Zero-Day Exploited to Dump NTLM Hashes and Gain SYSTEM Privileges"
date: 2026-04-23 08:00:36 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, cve, microsoft, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/recent-microsoft-defender-vulnerability-exploited-as-zero-day/
---

A recently disclosed Microsoft Defender vulnerability is being actively exploited in the wild.
Attackers leverage the flaw to access the Security Account Manager (SAM) database, extract NTLM
password hashes, and escalate privileges to SYSTEM level. SAM database access enables credential
dumping, which attackers use for lateral movement and further compromise across environments.

Organizations running Windows Defender should apply available patches immediately and audit endpoint
telemetry for signs of NTLM hash extraction or unauthorized SAM registry access. Detection rules
for SAM access patterns should be reviewed or added to endpoint monitoring given confirmed active
exploitation.
