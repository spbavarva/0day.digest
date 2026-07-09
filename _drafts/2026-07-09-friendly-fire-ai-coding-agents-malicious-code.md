---
title: "'Friendly Fire' Attack Tricks AI Code-Review Agents Into Running Malicious Code"
date: 2026-07-09 05:15:02 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, rce, anthropic, openai]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/friendly-fire-ai-agents-built-to-catch.html
---

The AI Now Institute has published a proof-of-concept called "Friendly
Fire," showing that asking an AI coding agent to scan open-source code
for vulnerabilities can instead cause the agent to execute the attacker's
malicious code on the reviewer's own machine. The technique works against
Anthropic's Claude Code and OpenAI's Codex when running in an autonomous
mode that self-approves actions. Teams using autonomous code-review agents
should avoid auto-approval modes when scanning untrusted repositories.
