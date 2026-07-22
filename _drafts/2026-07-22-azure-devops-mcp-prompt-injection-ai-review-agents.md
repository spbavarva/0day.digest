---
title: "Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents"
date: 2026-07-22 04:57:52 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, prompt-injection, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/microsoft-azure-devops-mcp-flaw-lets.html
---

A flaw in Microsoft's official Azure DevOps MCP server lets a single
hidden comment in a pull request hijack a reviewer's own AI coding agent.
The MCP server returns PR descriptions without stripping embedded
instructions, so an attacker's comment can redirect a reviewer's agent
into projects the attacker has no access to and exfiltrate what it finds.
It's an indirect prompt injection attack, notable for landing in a
first-party Microsoft AI integration rather than a third-party wrapper.
Teams using the Azure DevOps MCP server for AI-assisted review should
treat PR content as untrusted input until a fix ships.
