---
title: "Digitally Signed Adware Tool Deploys SYSTEM-Privilege Scripts to Disable Antivirus"
date: 2026-04-15 17:59:00 +0000
categories: [Daily Signal]
tags: [malware, privilege-escalation]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/signed-software-abused-to-deploy-antivirus-killing-scripts/
---

A digitally signed adware tool has been used to deploy payloads that execute with SYSTEM-level
privileges and disable antivirus protections across thousands of endpoints. Affected sectors
include education, utilities, government, and healthcare, suggesting broad distribution rather
than a targeted campaign.

Abuse of a legitimately signed executable bypasses application control policies and most
allowlisting tools, which trust certificates rather than behavior. From that trusted anchor, the
payload escalates to SYSTEM and terminates AV processes before deploying further stages—a
pattern common in ransomware pre-deployment.

Security teams should review application control and WDAC policies for signed-by-certificate
allowlisting that could be abused this way. Monitoring for unexpected SYSTEM-level process
spawning from signed non-OS binaries and AV service termination events are effective detection
signals.
