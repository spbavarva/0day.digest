---
title: "Cisco Talos Details CLOSEDQUORUM, First Reported Autonomous AI C2 Implant"
date: 2026-09-22 10:00:58 +0000
categories: [Daily Signal]
tags: [malware, llm, ai-safety, deepseek]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
---

CLOSEDQUORUM, a Windows malware binary discovered through Cisco Talos'
CAIRN project, exhibits fully autonomous command-and-control. It uses
Google Gemini, DeepSeek, Qwen, and Mistral AI models to independently
decide what actions to take during the post-compromise stages of an
attack.

Talos describes it as a shift in effort displacement for attackers, where
expanding portions of the attack chain run without operator involvement.
