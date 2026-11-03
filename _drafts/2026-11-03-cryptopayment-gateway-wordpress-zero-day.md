---
title: "Attackers Target Unpatched CryptoPayment Gateway Flaw That Can Expose Wallet Credentials"
date: 2026-11-03 05:34:37 +0000
categories: [Daily Signal]
tags: [vulnerability, zero-day, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-target-unpatched.html
---

Threat actors are actively exploiting an unpatched, maximum-severity
vulnerability in the CryptoPayment Gateway WordPress plugin, per findings
from Defused Cyber reported by The Hacker News. The flaw, CVE-2026-81648
(CVSS 10.0), could let unauthenticated attackers delete arbitrary files
on the server and extract data, potentially exposing wallet credentials.
No patch is currently available; site owners running this plugin should
disable or remove it until a fix ships.
