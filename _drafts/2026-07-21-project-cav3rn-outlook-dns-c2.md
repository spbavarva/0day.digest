---
title: "New Project CAV3RN Module Abuses Outlook Calendar and DNS for C2"
date: 2026-07-21 08:40:47 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/
---

Kaspersky GReAT describes a new module of Project CAV3RN, a
cyberespionage framework that communicates via Outlook calendar events
using Microsoft Graph. The module includes a backup communication channel
via DNS AAAA record responses, used for configuration recovery if the
primary calendar-based channel is disrupted.
