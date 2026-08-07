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

Researchers have attributed a supply chain attack on the Mastra npm
package ecosystem to North Korean threat actors. The attackers added a
malicious dependency to more than 140 Mastra packages that fetches a
payload designed to target cryptocurrency browser extensions. Mastra is
used in AI agent development, putting downstream projects that pulled
the compromised packages at risk of credential and wallet theft.
Developers who installed affected Mastra packages should audit their
dependency trees and rotate any exposed crypto wallet credentials.
