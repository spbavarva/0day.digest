---
title: "Researchers Build Self-Replicating AI Worm That Runs Entirely on Local Open-Weight Models"
date: 2026-06-09 11:59:03 +0000
categories: [Daily Signal]
tags: [malware, llm, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html
---

University of Toronto researchers published a proof-of-concept AI worm that uses a locally-hosted open-weight LLM to reason through a network autonomously, generating tailored attack strategies for each discovered target.
The worm replicates itself across hosts without human intervention and without contacting any commercial AI service — eliminating dependency on API keys, rate limits, or cloud connectivity.
This design makes the attack plausible in air-gapped or policy-restricted environments where commercial AI APIs are blocked.
The research is pre-print and PoC-stage, but the architecture represents a meaningful capability advance; AI-driven autonomous lateral movement no longer requires frontier model access.
