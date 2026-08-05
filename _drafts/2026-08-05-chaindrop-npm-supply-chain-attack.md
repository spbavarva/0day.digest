---
title: "Over 400 NPM Packages Infected in ChainDrop Supply Chain Attack"
date: 2026-08-05 08:56:58 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, github]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/
---

The ChainDrop supply chain attack has infected more than 400 npm
packages with malware designed to steal and exfiltrate secrets from
developer machines and CI environments.

The malware propagates itself further by using stolen npm and GitHub
credentials to compromise additional maintainer accounts, spreading
beyond the initially affected packages.

Developers who installed packages from the affected set should rotate
npm and GitHub credentials and audit recent CI activity for signs of
unauthorized publishes.
