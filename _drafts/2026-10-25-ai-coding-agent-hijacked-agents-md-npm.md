---
title: "AI Coding Agents Hijacked Using AGENTS.md File in Downloads Folder"
date: 2026-10-25 15:49:38 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, npm, supply-chain]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ai-coding-agents-hijacked-using-agentsmd-file-in-downloads-folder/
---

Researchers found a malicious AGENTS.md instruction file planted in a
customer's Downloads folder that tricked an AI coding agent into installing
a rogue npm package.

The file abused the agent's practice of reading markdown instruction files
for context, injecting instructions that led it to pull in
attacker-controlled code during a routine task.

Teams using AI coding agents should treat untrusted local markdown/config
files as a prompt injection vector and review what files their agents are
allowed to read automatically.
