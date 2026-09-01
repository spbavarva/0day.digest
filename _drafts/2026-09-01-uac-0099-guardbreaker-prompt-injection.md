---
title: "Russia-Aligned UAC-0099 Uses Prompt Injection to Disrupt AI-Assisted Malware Analysis"
date: 2026-09-01 08:26:24 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/russia-aligned-uac-0099-plants-nuclear.html
---

ESET disclosed a technique dubbed GuardBreaker used by the
Russia-aligned threat actor UAC-0099 against a target in Ukraine. The
malware embeds a prompt intended to trip a large language model's
safety mechanisms when the sample is fed to an AI assistant for
analysis, aiming to prevent the LLM from producing a usable summary of
the malicious code.

The technique reflects a growing category of anti-analysis tricks
aimed specifically at AI-assisted security tooling, distinct from
traditional anti-sandbox or anti-antivirus evasion.
