---
title: "Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws"
date: 2026-09-19 10:01:10 +0000
categories: [Daily Signal]
tags: [anthropic, openai, appsec, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
---

Researchers at security firm Hacktron used Anthropic's Claude Opus 5 to
chain two vulnerabilities together, taking over the ChatGPT and Codex
accounts of several OpenAI employees and ultimately reaching an
internal OpenAI code repository.

The chain began with a bug in the software running OpenAI's public
help forum and continued through a weakness in OpenAI's own login
system. The work was disclosed as authorized security research.
