---
title: "IronWorm Infostealer Hits 36 npm Packages in Supply-Chain Attack"
date: 2026-06-04 15:25:37 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, infostealer]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/
---

A new supply-chain attack has seeded 36 npm packages with IronWorm, an infostealer designed to exfiltrate credentials and secrets from developer environments. The campaign mirrors earlier malicious-package patterns but the scope—36 packages simultaneously—is broader than most recent incidents. Node.js developers should audit their dependency trees against the affected package list and check for IronWorm IOCs in endpoint telemetry. Any secrets or credentials that may have been loaded in environments where the affected packages ran should be rotated immediately.
