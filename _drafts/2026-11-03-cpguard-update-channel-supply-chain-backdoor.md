---
title: "cPGuard Update Channel Hijacked to Backdoor Linux Servers and Collect Password Hashes"
date: 2026-11-03 15:16:32 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, data-breach]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/cpguard-update-channel-hijacked-to.html
---

An attacker compromised the update system of the cPGuard security tool
on November 2 and used it to push a malicious script to customers'
Linux servers running cPGuard 5.88.25 and later. The script installed
a backdoor and collected password hashes and other sensitive files.

Maker OPSSHIELD says the attacker has exfiltrated some of that data.
Organizations running cPGuard should treat affected servers as
compromised, rotate credentials, and follow the vendor's incident
advisory.
