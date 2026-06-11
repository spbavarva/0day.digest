---
title: "'GreatXML' Zero-Day Exploit Bypasses BitLocker"
date: 2026-06-11 09:56:12 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, microsoft, privilege-escalation]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/
---

A newly disclosed zero-day exploit, dubbed "GreatXML," bypasses Windows BitLocker disk encryption.
The proof-of-concept abuses Microsoft Defender's offline scan feature to spawn a SYSTEM-level shell when a device reboots into Windows Recovery Mode.
Because the technique runs before the OS fully boots, an attacker with physical access could read or modify data on encrypted drives.
Organizations relying on BitLocker for at-rest protection on devices with physical exposure should watch for Microsoft's response and review Recovery Mode access controls in the meantime.
