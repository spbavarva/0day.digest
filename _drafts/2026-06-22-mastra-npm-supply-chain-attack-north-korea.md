---
title: "North Korean Hackers Blamed for Mastra NPM Supply Chain Attack"
date: 2026-06-22 11:10:06 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/north-korean-hackers-blamed-for-mastra-npm-supply-chain-attack/
---

SecurityWeek reports North Korean state-linked hackers have been blamed for a supply chain attack against the Mastra npm package ecosystem. A malicious dependency added to more than 140 Mastra packages fetches a payload that targets cryptocurrency browser extensions. Developers who installed affected Mastra packages should audit their dependency trees, remove the malicious packages, and rotate any credentials or wallet keys that may have been exposed.
