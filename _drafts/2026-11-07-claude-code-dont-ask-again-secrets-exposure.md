---
title: "Claude Code's \"Don't Ask Again\" Setting Exposed Secrets in 1,122 Public GitHub Repos"
date: 2026-11-07 06:44:17 +0000
categories: [Daily Signal]
tags: [anthropic, llm, appsec, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html
---

When a developer selects "Yes, and don't ask again" in Claude Code,
Anthropic's AI coding assistant can save the approved command word-for-word
into a project settings file — including any secret typed as part of that
command. Security firm Apiiro found passwords and API keys from these
saved commands sitting in 1,122 public GitHub repositories, readable by
anyone.

Teams using Claude Code should audit project settings files before
committing them and rotate any credentials that may already be exposed.
