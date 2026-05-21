---
title: "1Password and OpenAI Introduce Just-in-Time Credentials for AI Coding Agents"
date: 2026-05-20 13:34:54 +0000
categories: [Daily Signal]
tags: [iam, llm, openai, appsec]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/1password-teams-with-openai-to-stop-ai-coding-agents-from-leaking-credentials/
---

1Password has partnered with OpenAI to introduce a just-in-time (JIT) credential delivery model for OpenAI Codex. Under the approach, AI coding agents receive credentials injected at runtime that expire after use, keeping secrets out of prompts, code repositories, and model context windows.

The model addresses one of the most practical risks of agentic AI workflows: long-lived credentials accessible to the agent can be extracted via prompt injection or inadvertently included in generated code. Teams deploying AI coding agents with access to production systems or credentials should evaluate JIT credential patterns as part of their agent security posture.
