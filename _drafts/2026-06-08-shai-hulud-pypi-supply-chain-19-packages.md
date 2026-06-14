---
title: "Shai-Hulud Attack Trojanizes 19 Science-Focused PyPI Packages"
date: 2026-06-08 20:41:35 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-shai-hulud-attack-trojanizes-19-science-focused-pypi-packages/
---

A supply-chain campaign dubbed Shai-Hulud has compromised 19 PyPI packages
targeting the scientific Python ecosystem, with the affected libraries
collectively downloaded hundreds of thousands of times. Malicious versions
deliver malware designed to steal developer secrets including API keys, tokens,
and credentials from affected machines. All 19 packages were legitimate
science-focused libraries before the compromise. Developers using any affected
package should rotate credentials immediately, audit recent build outputs for
exfiltration activity, and remove or upgrade the flagged packages from their
environments.
