---
title: "ARToken Phishing-as-a-Service Panel Targets Microsoft 365"
date: 2026-07-01 10:00:38 +0000
categories: [Daily Signal]
tags: [phishing, malware, microsoft]
severity: medium
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
---

Cisco Talos identified ARToken, a phishing-as-a-service panel used by an
affiliate group called EvilTokens that targets Microsoft 365 accounts. The
panel exposes more than 80 API endpoints supporting device-code phishing,
Primary Refresh Token persistence, email access, business email
compromise, and SharePoint exfiltration. The breadth of the API surface
suggests a mature, productized PhaaS operation rather than a one-off kit.
Organizations should treat device-code phishing and PRT theft as active
threats and review conditional access policies accordingly.
