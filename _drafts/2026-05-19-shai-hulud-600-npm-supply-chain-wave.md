---
title: "New Shai-Hulud Wave Compromises 600+ npm Packages in Fresh Supply Chain Hit"
date: 2026-05-19 14:30:22 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-shai-hulud-malware-wave-compromises-600-npm-packages/
---

Threat actors published more than 600 malicious packages to the npm registry today as part of a new Shai-Hulud supply-chain campaign.
This is a continuation of a previously identified Shai-Hulud campaign that has now expanded in scope.
Developers who installed npm packages during the active window should audit their dependency trees for Shai-Hulud indicators and rotate any secrets that could have been accessed by the malicious packages.
Lock files should be committed and verified; `npm audit` alone may not surface recently-published malicious packages until registry metadata is updated.
Organizations with automated dependency update workflows (Dependabot, Renovate) should review recent PRs for packages introduced from the affected timeframe.
