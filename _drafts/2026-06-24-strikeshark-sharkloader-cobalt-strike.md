---
title: "StrikeShark: Investigating a New Campaign Delivering Cobalt Strike Through SharkLoader"
date: 2026-06-24 10:00:03 +0000
categories: [Daily Signal]
tags: [malware]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/strikeshark-campaign/120326/
---

Kaspersky's GReAT team detailed a new campaign, dubbed StrikeShark, that
delivers Cobalt Strike Beacon through a custom loader called
SharkLoader. The campaign appears global in scope based on the
researchers' telemetry. The write-up focuses on the loader's delivery
chain and detection opportunities rather than a specific vulnerability.
Defenders already monitoring for Cobalt Strike Beacon traffic should
add SharkLoader indicators to their detection coverage.
