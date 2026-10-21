---
title: "LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor"
date: 2026-10-21 18:01:57 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware, llm]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
---

The LiteLLM Python package was compromised in a software supply chain attack
that delivered a credential stealer and a backdoor, according to reports from
SafeDep, Socket, StepSecurity, and Upwind. The compromise affects LiteLLM
1.107.0, distributed through both PyPI wheels and Docker images.

The malicious release has since been quarantined on PyPI. LiteLLM is widely
used for routing calls across LLM providers, making this a supply chain risk
specifically for AI application pipelines. Teams that installed 1.107.0
should audit for credential exposure and rotate secrets accessible to
affected hosts.
