---
title: "OpenAI Rolls Out ChatGPT Lockdown Mode to Limit Prompt Injection Data Exfiltration"
date: 2026-06-06 13:36:57 +0000
categories: [Daily Signal]
tags: [llm, openai, ai-safety, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html
---

OpenAI has begun rolling out Lockdown Mode for ChatGPT, restricting tools that
could enable data exfiltration — particularly those exploitable through prompt
injection attacks. The feature targets users and organizations handling sensitive
data and is available across Free, Go, Plus, and Pro tiers for logged-in accounts.

Lockdown Mode reduces the attack surface for indirect prompt injection scenarios
where malicious content in documents or web pages hijacks ChatGPT's tool-use
actions to exfiltrate data. Organizations deploying ChatGPT in sensitive workflows
should evaluate enabling this feature as part of their LLM deployment security
controls.
