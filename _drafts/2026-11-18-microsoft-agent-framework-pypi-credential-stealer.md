---
title: "Microsoft's Agent Framework PyPI Package Compromised to Steal Credentials"
date: 2026-11-18 16:58:42 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware, microsoft]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/
  - name: SecurityWeek
    url: https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/
---

Hackers compromised Microsoft's official "agent-framework" Python package on
PyPI, publishing malicious versions 1.26.1 and 1.26.2 that steal Azure, Azure
DevOps, and GitHub Actions credentials when Python starts.

This is a supply chain compromise of a widely used Microsoft-maintained
package. Anyone who installed those versions should rotate the affected
credentials and pin to a clean release.
