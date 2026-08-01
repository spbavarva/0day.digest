---
title: "Kaspersky Details Network Anomaly Detection Rules in KATA"
date: 2026-07-31 10:00:25 +0000
categories: [Daily Signal]
tags: [malware, privilege-escalation]
severity: informational
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/tr/network-anomaly-detection-in-kata/120892/
---

Kaspersky's GReAT team published an analysis of how Network Anomaly
Detection (NAD) rules operate within Kaspersky Anti Targeted Attack (KATA),
using Kerberoasting and DNS tunneling as example detection scenarios.

The piece is primarily a defensive/detection-engineering writeup rather than
a new vulnerability or incident disclosure. It illustrates how NAD rules can
surface both credential-attack and covert-channel activity within
enterprise networks.
