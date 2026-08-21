---
title: "Encrypted Prompts Bypass AI Safety Guardrails in Grok and Gemini"
date: 2026-08-21 14:34:05 +0000
categories: [Daily Signal]
tags: [ai-safety, llm, prompt-injection, google]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/encrypted-prompts-bypass-ai-safety-guardrails-in-grok-and-gemini/
---

Researchers describe a new "Cryptographic Context Injection" technique that
conceals malicious instructions in encrypted form so safety filters can't
inspect them at input time. The payload is only decrypted once it reaches a
trusted execution environment inside the model pipeline, bypassing safety
guardrails in both Grok and Gemini. The technique highlights a gap in
guardrails that only inspect plaintext prompts.
