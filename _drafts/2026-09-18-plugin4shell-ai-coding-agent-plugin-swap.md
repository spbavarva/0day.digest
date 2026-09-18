---
title: "Plugin4Shell Flaw Lets Repo Owners Swap Pinned Plugins in AI Coding Agents"
date: 2026-09-18 11:01:01 +0000
categories: [Daily Signal]
tags: [supply-chain, llm, anthropic, openai, github]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html
---

Security firm Air Security disclosed a flaw, dubbed Plugin4Shell, in four
widely used AI coding agents: someone who controls a plugin's source
repository can swap the code an agent installs for a malicious version —
even when the agent had pinned that plugin to a specific reviewed
commit. Anthropic has patched the issue in Claude Code 2.1.179 and OpenAI
in Codex 0.146.0; GitHub Copilot's fix status was unclear at time of
reporting.
