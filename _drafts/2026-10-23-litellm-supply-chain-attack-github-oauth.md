---
title: "LiteLLM Compromised in Fresh Supply Chain Attack"
date: 2026-10-23 08:10:46 +0000
categories: [Daily Signal]
tags: [supply-chain, llm, pypi, github]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
---

LiteLLM, a widely used LLM proxy library, was hit by a new supply chain
attack. Attackers used compromised GitHub CLI OAuth tokens to push and
approve malicious packages on both PyPI and Docker.

Teams depending on LiteLLM should audit which package versions and
container images they've pulled recently and verify them against
known-good releases before trusting them in production.
