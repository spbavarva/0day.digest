---
title: "ARToken PhaaS Exposes EvilTokens' Microsoft 365 Phishing Toolkit"
date: 2026-07-03 14:12:22 +0000
categories: [Daily Signal]
tags: [phishing, microsoft]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/
---

Researchers uncovered "ARToken," a phishing-as-a-service platform that
appears to operate as an affiliate of the existing EvilTokens phishing
operation. The finding gives defenders visibility into an extensive
toolkit built to compromise Microsoft 365 accounts. Organizations should
enforce phishing-resistant MFA on Microsoft 365 accounts and review
sign-in logs for token-replay indicators, since PhaaS kits targeting M365
commonly harvest session tokens rather than just passwords.
