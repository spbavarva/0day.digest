---
title: "Microsoft Starts Removing WMIC Tool Used by Cybercriminals"
date: 2026-08-18 08:12:08 +0000
categories: [Daily Signal]
tags: [appsec, malware, microsoft]
severity: informational
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-removes-wmic-lolbin-tool-in-windows-11-beta-builds/
---

Microsoft has removed the Windows Management Instrumentation Command-line
(WMIC) tool from Windows 11 24H2, 25H2, and current Windows 11 beta
builds. WMIC has long been abused by attackers as a living-off-the-land
binary to execute commands and evade detection.

The removal reduces a commonly abused attack surface, though organizations
with scripts or tooling still dependent on WMIC should test for breakage
before the change reaches stable channels.
