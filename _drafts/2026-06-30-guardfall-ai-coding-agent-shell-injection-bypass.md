---
title: "GuardFall: Decades-Old Shell Trick Bypasses Safety Checks in AI Coding Agents"
date: 2026-06-30 14:26:15 +0000
categories: [Daily Signal]
tags: [supply-chain, llm, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html
  - name: SecurityWeek
    url: https://www.securityweek.com/decades-old-bash-tricks-expose-ai-coding-agents-to-supply-chain-attacks/
---

Security firm Adversa AI disclosed GuardFall, a technique that bypasses the
safety checks meant to stop AI coding agents from executing dangerous shell
commands. The bypass relies on a decades-old Bash/shell trick rather than a
novel exploit. Adversa tested eleven popular open-source coding and
computer-use agents and found ten were vulnerable; only one, Continue, was
built to resist the technique. The gap exposes affected agents to potential
supply chain attacks via malicious repositories.
