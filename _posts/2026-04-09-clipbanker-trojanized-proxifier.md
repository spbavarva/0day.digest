---
title: "ClipBanker Malware Distributed via Trojanized Proxifier in Multi-Stage Attack Chain"
date: 2026-04-09 09:30:17 +0000
categories: [Daily Signal]
tags: [malware, supply-chain, crypto]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/clipbanker-malware-distributed-via-trojanized-proxifier/119341/
---

Kaspersky GReAT researchers documented an active campaign distributing ClipBanker malware
through trojanized copies of Proxifier, a legitimate network proxy application. The fake installer
initiates a multi-stage infection chain that deploys a clipboard hijacker, which silently replaces
cryptocurrency wallet addresses copied by the victim with attacker-controlled addresses.

Victims initiating crypto transfers unknowingly send funds to the attacker. The trojanized
software closely mimics the real Proxifier UI, making detection difficult without signature-based
scanning. Users should download software exclusively from official vendor sites, verify digital
signatures before execution, and monitor clipboard contents when handling crypto transactions.
