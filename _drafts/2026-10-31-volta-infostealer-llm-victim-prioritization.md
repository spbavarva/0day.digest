---
title: "VOLTA Infostealer Uses LLMs to Rank Victims by Value"
date: 2026-10-31 12:00:00 +0000
categories: [Daily Signal]
tags: [malware, llm]
severity: medium
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/
---

Cisco Talos documented VOLTA, a self-deleting infostealer that harvests
credentials, session tokens, and cryptocurrency wallets.

Beyond standard theft, VOLTA feeds captured data to an LLM to profile victims
and rank which stolen assets are most valuable to the operator, automating a
triage step attackers previously did by hand.
