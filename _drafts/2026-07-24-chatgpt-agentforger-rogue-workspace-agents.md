---
title: "ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link"
date: 2026-07-24 11:53:55 +0000
categories: [Daily Signal]
tags: [openai, llm, vulnerability, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
---

Zenity Labs disclosed a critical vulnerability, codenamed AgentForger, in
OpenAI's ChatGPT Workspace Agents. A single phishing link could stealthily
build, authorize, and deploy an autonomous AI agent inside a victim
organization's workspace — without the target knowingly granting that
access. OpenAI has addressed the issue as of June 8. Organizations using
ChatGPT Workspace Agents should review agent authorization logs for the
period before the fix.
