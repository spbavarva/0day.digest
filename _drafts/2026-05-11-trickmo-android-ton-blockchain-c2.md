---
title: "TrickMo Android Banking Trojan Shifts C2 to TON Blockchain to Evade Takedowns"
date: 2026-05-11 09:03:02 +0000
categories: [Daily Signal]
tags: [malware, android]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/trickmo-android-banker-adopts-ton-blockchain-for-covert-comms/
---

A new TrickMo variant targeting European banking users routes its command-and-control traffic through The Open
Network (TON) blockchain, replacing traditional C2 infrastructure. Blockchain-hosted C2 is effectively immune
to domain takedowns and server seizures, and TON traffic blends in with legitimate cryptocurrency activity.
The variant also adds new malware commands beyond prior credential-theft capabilities.

TrickMo has been active since at least 2020 and continues to evolve evasion techniques with each generation.
Mobile security teams and financial institutions operating in Europe should update detection rules to flag
anomalous TON API calls from Android banking sessions and monitor for the updated TrickMo IOCs when they
become available from threat intel vendors.
