---
title: "ARToken Phishing-as-a-Service Panel Targets Microsoft 365 Accounts"
date: 2026-07-01 10:00:38 +0000
categories: [Daily Signal]
tags: [phishing, microsoft, malware, iam]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
---

Cisco Talos identified "ARToken," a fully-featured phishing-as-a-service panel
that shares infrastructure, API contracts, and operational patterns with the
EvilTokens platform previously documented by Sekoia and Microsoft. The panel
exposes more than 80 API endpoints supporting device code phishing and
Primary Refresh Token theft against Microsoft 365 accounts. Talos ties
ARToken to the same affiliate ecosystem as EvilTokens rather than a
standalone operation. Organizations relying on device code authentication
flows should review Conditional Access policies and monitor for anomalous
Primary Refresh Token issuance.
