---
title: "Backdoored PyTorch Lightning Package on PyPI Delivers Credential Stealer"
date: 2026-05-04 17:15:27 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware, infostealer]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/backdoored-pytorch-lightning-package-drops-credential-stealer/
---

A malicious version of the PyTorch Lightning package was published to the Python Package Index (PyPI) and delivers a credential-stealing payload. The infostealer targets browser-stored credentials, environment files (such as `.env` files containing API keys and tokens), and cloud service credentials.

PyTorch Lightning is widely used in machine learning and deep learning workflows, giving the supply chain compromise significant reach across AI and data science teams. Developers and ML engineers should audit their dependency trees for the malicious package version and immediately rotate any credentials stored in environment files, browser password managers, or cloud service configurations.

This follows a broader pattern of attackers targeting ML and AI toolchains as a path to cloud infrastructure and sensitive training data. Remove the malicious package, identify which systems may have loaded it, and treat all credentials accessible from those systems as compromised.
