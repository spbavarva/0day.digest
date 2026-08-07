---
title: "LastPass Confirms Data Breach Tied to Klue Supply Chain Attack"
date: 2026-06-23 13:58:25 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/
---

LastPass confirmed that hackers accessed customer data from its Salesforce
environment after stealing the company's OAuth tokens in the Klue supply
chain attack disclosed earlier this month. The incident ties LastPass to the
broader Klue compromise that has already affected other organizations using
the Klue Battlecards integration. Affected customers should review Salesforce
access logs for anomalous activity tied to OAuth grants from the Klue
integration and treat any data accessible through that integration as
exposed.
