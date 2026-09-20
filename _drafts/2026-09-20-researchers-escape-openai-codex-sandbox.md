---
title: "Researchers Escape OpenAI Codex Sandbox to Run Commands on Host"
date: 2026-09-20 12:00:00 +0000
categories: [Daily Signal]
tags: [llm, rce, openai, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/
---

Researchers found two ways to escape OpenAI's Codex sandbox, including
one that achieved command execution on the host machine even from the
sandbox's most locked-down mode. OpenAI has patched both issues.

The findings show that AI coding-agent sandboxes advertised as tightly
locked down can still have escape paths to the underlying host, a risk
worth tracking for any team running LLM-driven code execution tools.
