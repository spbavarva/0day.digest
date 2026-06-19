---
title: "Salesforce Disables Klue Integration After OAuth Token Abuse Exposes Customer Data"
date: 2026-06-19 09:03:57 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - name: SecurityWeek
    url: https://www.securityweek.com/cybersecurity-firms-impacted-by-klue-supply-chain-attack/
---

Salesforce disabled the Klue Battlecards app integration on its platform
after OAuth tokens tied to the competitive-intelligence vendor were abused to
access customer Salesforce instances, following an incident first detected
June 11, 2026. Cybersecurity vendors Huntress and Recorded Future are among
the Klue customers whose Salesforce data was exfiltrated. Organizations
cannot currently reconnect to Salesforce via the Klue app until further
notice. This adds to a pattern of incidents involving abused OAuth tokens for
third-party Salesforce app integrations. Affected customers should audit
Salesforce login/API history for the relevant window and rotate any
credentials tied to the Klue integration.
