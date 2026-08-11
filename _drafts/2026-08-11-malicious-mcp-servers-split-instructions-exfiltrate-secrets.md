---
title: "Malicious MCP Servers Can Split Instructions to Make AI Coding Agents Exfiltrate Secrets"
date: 2026-08-11 10:24:00 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/malicious-mcp-servers-can-split.html
---

Researchers found that a malicious MCP tool server connected to an AI
coding assistant can exfiltrate SSH keys, environment secrets, source
code, and customer data without issuing any single instruction that looks
obviously harmful. The technique works by splitting a data-theft request
into fragments that each appear routine, placing them in channels the
assistant already uses, and can succeed even after the agent has refused
a blunter version of the same request.
