---
title: "Kaspersky Details Project CAV3RN Cyberespionage Framework"
date: 2026-07-21 08:40:47 +0000
categories: [Daily Signal]
tags: [malware, cyberespionage]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/
---

Kaspersky's GReAT researchers detailed a new C2 module used in "Project
CAV3RN," a cyberespionage framework. The module communicates via Microsoft
Graph by abusing Outlook calendar events, giving it a channel that blends
into normal Microsoft 365 traffic. A backup channel recovers configuration
data through DNS AAAA record responses, providing resilience if the primary
channel is blocked. Defenders monitoring for anomalous calendar-based API
activity or unusual DNS AAAA lookups may be able to detect this technique.
