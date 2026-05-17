---
title: "Tycoon2FA PhaaS Kit Adds Device-Code Phishing to Hijack Microsoft 365"
date: 2026-05-17 14:43:10 +0000
categories: [Daily Signal]
tags: [phishing, microsoft, iam]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/
---

The Tycoon2FA phishing-as-a-service kit has added device-code phishing support,
allowing attackers to bypass MFA and hijack Microsoft 365 accounts without stealing
passwords. The kit abuses Trustifi click-tracking URLs to mask redirect chains and
evade detection. Device-code phishing works by tricking users into entering a
legitimate-looking device code, which grants the attacker a valid OAuth session token.
Defenders should audit Entra ID conditional access policies to restrict or block the
device-code grant flow where it is not operationally required, and monitor for
unexpected `urn:ietf:params:oauth:grant-type:device_code` token requests in sign-in logs.
