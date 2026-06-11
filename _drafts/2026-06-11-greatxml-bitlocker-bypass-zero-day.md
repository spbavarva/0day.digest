---
title: "GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files"
date: 2026-06-11 17:43:52 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, privilege-escalation, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-greatxml-exploit-bypasses-windows.html
  - name: SecurityWeek
    url: https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/
---

Security researcher Chaotic Eclipse (aka Nightmare-Eclipse/MSNightmare) released GreatXML, a new unpatched bypass for Windows BitLocker that abuses recovery partition XML files.
The proof-of-concept exploits Microsoft Defender's offline scan feature to spawn a SYSTEM shell when a device reboots into Recovery Mode, defeating BitLocker's disk encryption protections.
The researcher says the discovery took roughly four hours and follows their earlier exploit targeting Microsoft Defender, published a day prior.
No official Microsoft patch is available yet.
Organizations relying on BitLocker for data-at-rest protection on lost or stolen devices should treat physical access as a higher-risk scenario until a fix ships.
