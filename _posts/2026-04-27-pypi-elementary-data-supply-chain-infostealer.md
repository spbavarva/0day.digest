---
title: "PyPI Package 'elementary-data' with 1.1M Monthly Downloads Backdoored to Steal Credentials"
date: 2026-04-27 15:17:37 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/pypi-package-with-11m-monthly-downloads-hacked-to-push-infostealer/
---

An attacker compromised the `elementary-data` PyPI package and published a malicious version targeting sensitive developer data and cryptocurrency wallets. The package receives approximately 1.1 million downloads per month, making this a high-impact supply chain attack.

Developers and organizations using `elementary-data` should immediately audit installed versions, rotate any credentials present in affected environments, and review CI/CD logs for data exfiltration activity. Verify pinned dependency hashes if this package appears in `requirements.txt` or lock files. Downstream pipelines that pulled the compromised version should be treated as potentially exfiltrated.
