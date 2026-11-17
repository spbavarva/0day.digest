---
title: "Simon Willison Details \"External Sandbox\" Pattern for Safer Coding Agents"
date: 2026-11-17 22:52:29 +0000
categories: [Daily Signal]
tags: [llm, ai-safety]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/
---

Simon Willison, working with Prime Radiant (the lab behind Superpowers),
published a write-up on an "external sandbox" pattern for code executed by
AI coding agents. In this design the agent itself runs outside the sandbox
while the code it generates executes inside an isolated environment,
reducing the risk that a mistake or a prompt injection attack could let a
model take damaging actions on the host machine.

The approach targets a gap in most current agent sandboxing, which isolates
the agent's reasoning but not necessarily the code it writes and runs.
Willison's post links to a demonstration of the pattern on the Prime
Radiant blog.
