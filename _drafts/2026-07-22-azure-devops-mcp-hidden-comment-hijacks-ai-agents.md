---
title: "Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents"
date: 2026-07-22 04:57:52 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, microsoft, azure, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/microsoft-azure-devops-mcp-flaw-lets.html
---

A flaw in Microsoft's official Azure DevOps MCP server lets a single
invisible comment in a pull request hijack a reviewer's own AI coding
agent. The issue stems from a tool that returns pull request descriptions
without a prompt-injection guardrail, letting an attacker-controlled
comment redirect the agent into projects it has no rights to access and
quietly leak what it finds. This is a concrete example of prompt injection
turning a code-review agent into a data-exfiltration vector.
