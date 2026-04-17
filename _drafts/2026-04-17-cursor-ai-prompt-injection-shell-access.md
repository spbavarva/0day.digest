---
title: "Cursor AI Prompt Injection Chains to Sandbox Bypass and Developer Shell Access"
date: 2026-04-17 07:29:00 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, appsec, privilege-escalation]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/cursor-ai-vulnerability-exposed-developer-devices/
---

A vulnerability in Cursor AI allows an indirect prompt injection to be chained with a
sandbox bypass and Cursor's built-in remote tunnel feature, resulting in shell access to
the developer's host machine.

The attack requires no special privileges. Any untrusted codebase, open-source repository,
or file opened within Cursor can carry the injected payload. When Cursor processes the
malicious content as context, the injected instructions can execute as if they came from
the legitimate user.

Developers using Cursor in agentic or file-reading workflows should treat untrusted code
with the same caution as executable input. This is the second major prompt injection
finding targeting AI coding assistants in recent weeks, following the "Comment and Control"
disclosure that affected Claude Code, Gemini CLI, and Copilot.
