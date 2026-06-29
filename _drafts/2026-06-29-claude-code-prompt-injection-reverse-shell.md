---
title: "Researchers Demonstrate Claude Code Attack That Hijacks Developer Machines via Booby-Trapped Repos"
date: 2026-06-29 14:28:40 +0000
categories: [Daily Signal]
tags: [llm, rce, ai-safety, anthropic]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/new-attack-abuses-claude-code-and-harmless-looking-repositories-to-hijack-developer-machines/
---

Researchers demonstrated an attack against Claude Code in which indirect
prompt injection hidden inside an apparently harmless repository causes the
tool to spawn a reverse shell on the developer's machine. Simply having
Claude Code process the repository's contents is enough to trigger the
malicious instructions.

The technique gives an attacker remote access to a developer's environment
without requiring the developer to run any code directly. It underscores the
risk of AI coding agents processing untrusted repository content with
elevated local privileges.
