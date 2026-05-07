---
title: "PyTorch Lightning Compromised in PyPI Supply Chain Attack to Steal Credentials"
date: 2026-04-30 16:31:00 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware, credential-theft]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html
---

Threat actors compromised the `lightning` PyPI package (PyTorch Lightning) and pushed two malicious versions — 2.6.2 and 2.6.3 — both published on April 30, 2026. The payloads are designed to steal credentials from infected developer environments. Aikido Security, Socket, and StepSecurity independently confirmed the campaign and assess it as an extension of a prior supply chain operation.

PyTorch Lightning is a widely-used training framework in ML and AI development pipelines. Developers or CI systems that installed either malicious version should roll back to 2.6.1 or earlier immediately and rotate any credentials, API keys, or cloud tokens that were present in the build environment.
