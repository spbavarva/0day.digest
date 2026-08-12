---
title: "Researchers Demonstrate Stealing Reasoning Traces From Proprietary LLM APIs"
date: 2026-08-11 22:40:45 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything
---

A new paper shows that encrypted chain-of-thought blocks returned by
Anthropic, OpenAI, and Google APIs can be replayed across sessions, users,
and even different models.

Researchers took a reasoning trace produced by a frontier model, replayed
it into a weaker sibling model, jailbroke that weaker model, and recovered
the stronger model's hidden reasoning in plaintext.

The technique raises confidentiality concerns for any provider that
returns encrypted-but-replayable reasoning traces to API clients.
