---
title: "Comment and Control: Claude Code, Gemini CLI, and GitHub Copilot Vulnerable to Prompt Injection via Code Comments"
date: 2026-04-16 08:33:00 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, appsec, anthropic, github, google]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/
---

A researcher has publicly disclosed an AI attack technique dubbed "Comment and Control"
affecting Claude Code, Gemini CLI, and GitHub Copilot agents. The method embeds adversarial
instructions inside ordinary code comments; when an AI coding assistant reads the file as
context, it executes the injected commands as if they were legitimate user instructions.

The attack requires no special privileges — any code repository, open-source project, or
file shared with a developer can carry the payload. Affected coding agents include tools
that read files from disk or repositories as part of their context window, making the
attack surface broad across any agentic workflow that processes untrusted code.

Developers using agentic AI tools should treat code from untrusted sources with the same
caution as executable input, and vendors should implement comment-stripping or trust-
boundary controls before feeding file contents to agent context.
