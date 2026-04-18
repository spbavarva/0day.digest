---
title: "Tycoon 2FA Disrupted but Its Tools Fuel Surge in AiTM Phishing Kits"
date: 2026-04-18 10:30:00 +0000
categories: [Daily Signal]
tags: [phishing, malware]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/tycoon-2fa-loses-phishing-kit-crown-amid-surge-in-attacks/
---

Following disruption of the Tycoon 2FA phishing-as-a-service (PhaaS) platform, threat
actors are reusing its tools and techniques across competing phishing kits, contributing
to a broader surge in adversary-in-the-middle (AiTM) style attacks. Tycoon 2FA had been
one of the most widely used PhaaS platforms for bypassing MFA via session token theft.

The proliferation of Tycoon 2FA tooling into other kits means defenders cannot rely on
blocking the original platform's infrastructure alone — the techniques live on in successor
kits. The AiTM phishing model targets session tokens rather than passwords, making
traditional MFA ineffective against it.

Organizations should enforce phishing-resistant MFA (FIDO2 / hardware security keys)
wherever possible. Conditional Access policies that validate device compliance and flag
anomalous session reuse add additional friction against AiTM-harvested tokens.
