---
title: "AI Coding Agents Leak Thousands of Secrets to Public GitHub Repos"
date: 2026-11-10 18:46:22 +0000
categories: [Daily Signal]
tags: [llm, appsec, github, data-breach]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyber-risk/ai-coding-agents-leak-secrets-github
---

A command in Claude Code has been inadvertently saving files containing
credentials and other sensitive data to public Git repositories,
according to Dark Reading. The behavior has reportedly led to thousands
of secrets being exposed in public repos tied to organizations using the
tool. Teams using AI coding agents should audit recent commits for
accidentally committed credentials and add pre-commit secret scanning
where it isn't already in place.
