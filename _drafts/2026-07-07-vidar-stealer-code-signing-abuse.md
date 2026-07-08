---
title: "Vidar Stealer Campaign Combines Code Signing Abuse and Go Loaders"
date: 2026-07-07 22:00:21 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/
---

Unit 42 detailed a cybercrime campaign delivering Vidar Stealer through a
loader-as-a-service framework combined with DLL sideloading via a
Go-compiled fake MpClient.dll. The campaign layers in code signing abuse and
file inflation as additional evasion techniques, a combination Unit 42
describes as novel. Defenders should watch for anomalous DLL sideloading
involving Microsoft-named binaries and unusually large binary file sizes.
