---
title: "Gentlemen Ransomware Integrates SystemBC for Bot-Powered Corporate Attacks"
date: 2026-04-20 20:02:37 +0000
categories: [Daily Signal]
tags: [ransomware, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/the-gentlemen-ransomware-now-uses-systembc-for-bot-powered-attacks/
---

An investigation into a Gentlemen ransomware attack revealed that the gang's affiliate has
integrated SystemBC proxy malware, building a command-and-control botnet of more than 1,570
compromised hosts — believed to be corporate victims — used to support ongoing attacks.

SystemBC is a SOCKS5 proxy and RAT that has been used by multiple ransomware groups
(including Ryuk and Conti affiliates) to establish persistent, encrypted C2 channels and
facilitate lateral movement inside compromised networks. Its adoption by Gentlemen signals
growing affiliate sophistication and a shared-tooling economy among ransomware operators.

Defenders should hunt for SystemBC IOCs in network telemetry, particularly outbound SOCKS5
proxy connections to unexpected destinations, and treat any Gentlemen-linked initial access
as an indicator that the full SystemBC toolkit may already be deployed.
