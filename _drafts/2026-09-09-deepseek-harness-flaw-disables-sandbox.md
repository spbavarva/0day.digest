---
title: "DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval"
date: 2026-09-09 11:17:07 +0000
categories: [Daily Signal]
tags: [llm, deepseek, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
---

A flaw in DeepSeek Harness, DeepSeek's open-source tool for running AI coding
agents on a developer's machine, let a sandboxed agent turn off its own
sandbox with a single command. The tool normally runs an agent's commands
inside an OS-level sandbox so it cannot write outside its workspace; the
agent could remove that limit by calling the tool's own web-facing controls.
Developers running DeepSeek Harness should update and review agent
permissions.
