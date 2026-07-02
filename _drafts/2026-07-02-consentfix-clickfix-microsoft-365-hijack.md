---
title: "ConsentFix and ClickFix Attacks Hijack Microsoft 365 Accounts in Seconds"
date: 2026-07-02 14:00:10 +0000
categories: [Daily Signal]
tags: [phishing, iam]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/consentfix-and-clickfix-how-microsoft-365-accounts-are-hijacked-in-3-seconds/
---

BleepingComputer details ConsentFix and ClickFix, two attack techniques
that steal Microsoft 365 authentication tokens within seconds using fake
prompts and abused OAuth consent flows. Both function as MFA bypass
methods, tricking users into authorizing malicious OAuth applications or
pasting attacker-supplied commands. Defenders should review OAuth app
consent policies and restrict user consent grants for third-party
applications where possible.
