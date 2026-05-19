---
title: "EvilTokens PhaaS Bypasses MFA via OAuth Device Code Flow, Hits 340 Orgs"
date: 2026-05-19 11:30:00 +0000
categories: [Daily Signal]
tags: [phishing, iam, microsoft, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html
---

EvilTokens, a phishing-as-a-service platform launched in February 2026, compromised more than 340 Microsoft 365 organizations across five countries within five weeks.
The technique abuses the OAuth device code flow: victims receive a message asking them to enter a short code at `microsoft.com/devicelogin` and complete their normal MFA challenge.
Because the victim authenticates legitimately with Microsoft, MFA is satisfied — but the resulting access token is captured by the attacker.
The attack bypasses all standard MFA controls and leaves no phishing artifacts on attacker-controlled infrastructure.
Organizations should audit Conditional Access policies to restrict or disable the device code flow where it is not operationally required, and review sign-in logs for suspicious device code grants.
