---
title: "Leaked Shai-Hulud Malware Fuels New npm Infostealer Campaign"
date: 2026-05-18 17:28:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/
---

The Shai-Hulud infostealer, whose source code leaked publicly last week, has been weaponized in a new campaign targeting the npm registry. Attackers repurposed the leaked malware to build infected npm packages appearing over the weekend. The campaign targets developer credentials and secrets stored in local environments and CI/CD pipelines. This follows a now-established pattern of treating leaked malware source as a rapid-deployment kit for new supply chain operations. Developers and teams should audit recently installed npm packages, verify integrity hashes, and review CI/CD secret exposure.
