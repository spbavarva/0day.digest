---
title: "Hackers Trojanize TrueConf Installers With Backdoors"
date: 2026-08-08 14:16:23 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-breach-trueconf-to-trojanize-client-installers-with-backdoors/
---

The Head Mare hacktivist group has been exploiting vulnerabilities in
unpatched TrueConf video conferencing servers to replace legitimate client
installers with trojanized versions that deliver backdoors. Because the
installers are swapped on the compromised server itself rather than at a
central distribution point, exposure depends on which organizations run
unpatched, internet-facing TrueConf instances. Users who downloaded
installers from an affected server during the compromise window may have
received a backdoored client. Organizations running TrueConf should patch
servers, verify installer integrity, and audit for indicators of compromise
from recently distributed client packages.
