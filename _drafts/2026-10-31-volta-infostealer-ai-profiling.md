---
title: "VOLTA Infostealer Uses LLMs to Prioritize Victims"
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
credentials, session tokens, and cryptocurrency wallets from infected
machines. After collection, VOLTA feeds the stolen data to an LLM, which
ranks victims by the value of their assets to prioritize follow-on abuse.

It's a concrete example of malware operationalizing AI inside the payload
itself, rather than AI tooling being used only to build or deliver it.
