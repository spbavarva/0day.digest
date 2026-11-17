---
title: "Lack of Ownership Verification on Hugging Face Let Researchers Hijack Kokoro TTS Account"
date: 2026-11-17 18:21:24 +0000
categories: [Daily Signal]
tags: [supply-chain, llm]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/researchers-hijack-hugging-face-account-for-popular-kokoro-ai-model/
---

Researchers demonstrated that a lack of ownership verification on Hugging
Face allowed them to take control of the account hosting Kokoro, a popular
text-to-speech model used in projects from Google, NVIDIA, AMD, Intel, and
AWS. A malicious actor exploiting the same gap could have pushed a tampered
model to numerous downstream consumers.

The researchers disclosed the issue rather than exploiting it maliciously.
The finding highlights a supply-chain risk specific to ML model hubs:
unlike package registries, model-hosting platforms may lack mature
account/namespace ownership controls.
