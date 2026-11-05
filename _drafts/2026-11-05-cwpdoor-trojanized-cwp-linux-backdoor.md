---
title: "Hackers Backdoor Linux Servers Using Trojanized CWP Web Server"
date: 2026-11-05 16:24:26 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-backdoor-linux-servers-using-trojanized-cwp-web-server/
---

A new Linux malware family called CWPdoor is being distributed through a
trojanized version of cwpsrv, the web server behind the Control Web Panel
(CWP) hosting management interface. Compromised cwpsrv installations give
attackers a persistent backdoor into affected Linux servers.

Administrators running Control Web Panel should verify the integrity of
their cwpsrv binaries against known-good checksums and audit for
unauthorized access.
