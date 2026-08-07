---
title: "Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets"
date: 2026-08-07 08:18:35 +0000
categories: [Daily Signal]
tags: [github, anthropic, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html
---

A GitHub issue opened by an account with no repository privileges was
enough to execute code on the CI runners behind Anthropic's and Google's
own coding-agent repositories, using Claude Code and Gemini CLI
respectively. On OpenAI's agent repository, the same class of flaw was
enough to hijack the next agent run. Novee Security ran the attacks against
each vendor's default configuration and presented the work at Black Hat
USA on August 5.
