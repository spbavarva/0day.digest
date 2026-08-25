---
title: "A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw"
date: 2026-08-25 14:07:37 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/a-malicious-webpage-could-poison-your.html
---

Oasis Security disclosed a weakness in NVIDIA NemoClaw that lets an
attacker-controlled webpage take unauthenticated control of a local Ollama
instance serving an AI agent. Once in control, the attacker can plant hidden
instructions inside the model itself, effectively poisoning the agent's
behavior from a page the victim simply visits in a browser. Oasis reported
the issue to NVIDIA's Product Security Incident Response Team ahead of
public disclosure. The flaw is a reminder that locally hosted LLM runtimes
reachable from a browser context need the same authentication scrutiny as
any other network-exposed service. Users running NemoClaw-based local AI
agents should check for a patch or mitigation guidance from NVIDIA.
