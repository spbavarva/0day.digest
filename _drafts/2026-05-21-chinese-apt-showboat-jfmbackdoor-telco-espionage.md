---
title: "Chinese APT Deploys Showboat and JFMBackdoor Against Telecom Providers"
date: 2026-05-21 14:00:00 +0000
categories: [Daily Signal]
tags: [malware, apt, espionage]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware/
---

Researchers disclosed two malware families used by Chinese state-sponsored actors in an
espionage campaign targeting telecommunications providers in the Middle East and Central Asia,
active since at least mid-2022. Showboat is a modular Linux post-exploitation framework with
remote shell, file transfer, and SOCKS5 proxy capabilities; JFMBackdoor is a companion Windows
implant.

Multiple Chinese APT groups appear to share the Showboat codebase, suggesting coordinated
tooling across threat clusters. The campaign's multi-year dwell time implies deep network
persistence; telcos in the region should audit Linux and Windows endpoints for indicators of
compromise.
