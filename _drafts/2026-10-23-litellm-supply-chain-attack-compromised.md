---
title: "LiteLLM Compromised in Fresh Supply Chain Attack"
date: 2026-10-23 08:10:46 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, github, llm]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
---

LiteLLM, a widely used library for calling multiple LLM providers through
a single interface, was compromised in a supply chain attack.

Attackers used compromised GitHub CLI OAuth tokens to push and approve
malicious packages to both PyPI and Docker Hub under the LiteLLM project.
Anyone who pulled LiteLLM packages or container images during the
compromise window should audit for unexpected versions and rotate any
credentials potentially exposed to the malicious build.
