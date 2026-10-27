---
title: "OpenAI Compaction Feature Flaw Let Researchers Extract Hidden Reasoning Text"
date: 2026-10-27 08:22:43 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, vulnerability, openai]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/openai-compaction-flaw-let-researchers.html
---

Security firm Xint showed that OpenAI's conversation "compaction"
feature, meant to shrink long conversations to save space, could be
abused to copy a reasoning model's hidden chain-of-thought out in plain
text. Normally, OpenAI's reasoning models return only an encrypted
representation of their internal reasoning, which users cannot read
directly.

The compaction bypass reportedly got around this protection, exposing
reasoning content meant to stay hidden. The finding matters for AI safety
since hidden-reasoning protections are often relied on to prevent leakage
of unsafe intermediate reasoning or to protect model IP.
