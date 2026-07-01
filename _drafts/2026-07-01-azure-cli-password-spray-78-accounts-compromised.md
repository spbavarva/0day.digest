---
title: "Azure CLI Password Spray Compromises 78 Microsoft Accounts in 81M+ Attempts"
date: 2026-07-01 05:46:03 +0000
categories: [Daily Signal]
tags: [azure, microsoft, iam]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
  - name: SecurityWeek
    url: https://www.securityweek.com/massive-password-spray-campaign-targeting-azure-cli/
---

Huntress researchers identified a massive, ongoing, automated password spray
campaign against Microsoft's Azure CLI, originating from an IPv6 range
(2a0a:d683::/32) controlled by hosting provider LSHIY LLC (AS32167). Between
June 12 and June 26, the campaign generated more than 81 million login
attempts and compromised at least 78 Microsoft accounts. Organizations
should review Azure CLI sign-in logs for attempts from this IP range and
enforce conditional access and MFA on affected accounts.
