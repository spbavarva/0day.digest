---
title: "GhostApproval Symlink Flaw Lets Malicious Repos Hijack AI Coding Agents"
date: 2026-07-09 04:27:18 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, rce, anthropic, aws]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
---

Wiz researchers disclosed "GhostApproval," a symlink-based flaw affecting
six popular AI coding assistants: Amazon Q Developer, Anthropic's Claude
Code, Augment, Cursor, Google Antigravity, and Windsurf. A booby-trapped
code project can get the agent to ask permission to edit one
harmless-looking file, but the write actually lands on a sensitive file
instead, letting the malicious repo take control of the developer's
machine. Teams should treat human-approval prompts in these tools as
insufficient protection against untrusted repositories until patched.
