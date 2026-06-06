---
title: "OpenAI Launches Lockdown Mode to Limit Data Exfiltration from Prompt Injection Attacks"
date: 2026-06-05 23:56:40 +0000
categories: [Daily Signal]
tags: [openai, ai-safety, llm, appsec]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything
---

OpenAI has begun rolling out Lockdown Mode to personal and self-serve business ChatGPT accounts after previewing the feature in February. The mode limits outbound network requests that could transfer sensitive data to an attacker following a successful prompt injection. Lockdown Mode does not prevent prompt injections from reaching ChatGPT — it targets the final exfiltration step — so it remains a partial mitigation. The feature is rolling out to Free, Go, Plus, Pro, and self-serve Business accounts. Organizations using ChatGPT with sensitive data should enable Lockdown Mode to reduce blast radius from prompt injections delivered via uploaded files or cached web content.
