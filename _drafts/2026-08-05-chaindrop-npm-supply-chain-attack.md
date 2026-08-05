---
title: "Over 400 NPM Packages Infected in ChainDrop Supply Chain Attack"
date: 2026-08-05 08:56:58 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/
---

Malware dubbed ChainDrop has infected more than 400 npm packages. The
malware is designed to steal and exfiltrate secrets, and to propagate
itself further using stolen npm and GitHub credentials.

Given the self-propagating design and the number of packages already
affected, teams should audit CI/CD secrets and npm/GitHub credentials used
in affected pipelines and rotate any that may have been exposed.
</content>
