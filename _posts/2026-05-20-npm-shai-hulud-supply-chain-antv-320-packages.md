---
title: "Over 320 NPM Packages Hit by Fresh Mini Shai-Hulud Supply Chain Attack"
date: 2026-05-20 11:06:49 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/over-320-npm-packages-hit-by-fresh-mini-shai-hulud-supply-chain-attack/
---

A compromised maintainer account in the @antv namespace was used to publish malicious versions across 320+ npm packages in a fresh wave dubbed "Mini Shai-Hulud." The @antv namespace is widely used for data visualization in JavaScript applications, giving this attack significant blast radius across the frontend ecosystem.

Any project that recently installed or updated @antv packages should audit its lock files for unexpected version bumps. Check `package-lock.json` or `yarn.lock` for @antv entries published around the time of the incident and compare hashes against known-good releases. Rotate any secrets present in environments where the affected packages may have executed.
