---
title: "New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets"
date: 2026-06-11 17:46:32 +0000
categories: [Daily Signal]
tags: [llm, prompt-injection, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
---

Two separate research teams demonstrated that OpenClaw, a popular self-hosted AI agent, can be manipulated into executing attacker-controlled code or exfiltrating sensitive data through ordinary-looking inputs.
Imperva researchers hid malicious instructions inside shared contacts, vCards, and location pins that the agent processed and acted on without the victim seeing them.
Varonis built a separate proof-of-concept demonstrating a related credential-leaking attack chain.
Both attacks rely on prompt injection via everyday data formats rather than traditional software exploits.
Operators of self-hosted AI agents should review which input sources are auto-processed and restrict agent permissions accordingly.
