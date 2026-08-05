---
title: "Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports"
date: 2026-08-05 15:14:05 +0000
categories: [Daily Signal]
tags: [rce, llm, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/paperclip-ai-flaws-let-attackers-run.html
---

Two security flaws in Paperclip, an open-source control plane for teams of
AI agents, let attackers execute commands on a network server or a
developer's machine. Both paths are triggered by importing a malicious
agent and starting it.

A third flaw could expose sensitive data and control-plane details through
API routes. Teams running Paperclip should treat agent imports as untrusted
code and review who can start agents on shared infrastructure.
</content>
