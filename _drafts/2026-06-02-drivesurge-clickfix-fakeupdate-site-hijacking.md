---
title: "DriveSurge Campaign Hijacks Thousands of Websites for ClickFix and FakeUpdate Attacks"
date: 2026-06-01 22:14:19 +0000
categories: [Daily Signal]
tags: [malware, phishing, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-hijack-thousands-of-sites-for-clickfix-and-fakeupdate-attacks/
---

A threat actor tracked as DriveSurge is operating large-scale malware distribution
campaigns by compromising thousands of legitimate websites and injecting ClickFix and
FakeUpdate lures. Visitors are presented with fake browser update prompts or CAPTCHA
pages that execute malicious PowerShell when clicked.

The infrastructure relies on high volumes of compromised sites rather than a central
C2 domain, making takedowns difficult. Website owners should audit for unauthorized
JavaScript injections; defenders should block known DriveSurge IOCs at the proxy and
DNS layers.
