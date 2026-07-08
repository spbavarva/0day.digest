---
title: "Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection"
date: 2026-07-08 10:30:55 +0000
categories: [Daily Signal]
tags: [github, llm, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/critical-vulnerability-exposes-github-agentic-workflows-to-prompt-injection/
---

Researchers demonstrated that a crafted public GitHub Issue can trick
AI-powered agentic workflows into exposing data from private repositories
without authentication. The attack relies on prompt injection embedded in
issue content that the workflow's AI agent processes with elevated
repository access. Teams running AI agents against untrusted GitHub Issue
content should review workflow permissions and treat issue text as
untrusted input.
