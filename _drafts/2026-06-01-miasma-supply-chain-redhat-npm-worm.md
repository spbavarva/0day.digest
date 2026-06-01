---
title: "Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm"
date: 2026-06-01 17:40:28 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, github]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
---

A supply chain campaign dubbed Miasma has compromised @redhat-cloud-services packages on npm, deploying a credential-stealing worm that spreads via install-time execution and targets CI/CD pipelines. Researchers link the tactics to the prior Shai-Hulud campaign family: install-time code execution, credential harvesting from developer machines, CI/CD secret targeting, and encrypted exfiltration.

Any developer machine that executed an install of an affected package should be treated as potentially compromised. Immediately rotate all secrets stored in environment variables, CI/CD pipeline secrets, and local `.env` files. Audit `package.json` scripts in affected projects for unexpected `postinstall` hooks and review npm audit output for the affected packages.
