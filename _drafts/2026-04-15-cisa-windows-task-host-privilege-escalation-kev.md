---
title: "CISA Adds Windows Task Host Privilege Escalation Flaw to Known Exploited Vulnerabilities"
date: 2026-04-15 14:51:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation, microsoft]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisa-flags-windows-task-host-vulnerability-as-exploited-in-attacks/
---

CISA has added a Windows Task Host privilege escalation vulnerability to its Known Exploited
Vulnerabilities catalog after confirming exploitation in the wild. The flaw allows attackers who
have already gained a foothold on a Windows system to elevate to SYSTEM-level privileges.

A KEV addition represents confirmed in-the-wild exploitation, not theoretical risk. Privilege
escalation to SYSTEM is a critical step in post-exploitation chains, enabling credential
dumping, persistence mechanisms, and lateral movement within a network.

Federal agencies are subject to BOD 22-01 remediation deadlines. All organizations running
Windows should treat this as a priority patch, prioritizing internet-exposed and domain-joined
endpoints. Consult CISA's KEV catalog for the specific CVE identifiers and affected version
ranges.
