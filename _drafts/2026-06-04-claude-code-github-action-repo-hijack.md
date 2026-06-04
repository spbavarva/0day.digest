---
title: "Claude Code GitHub Action Flaw Enabled Single-Issue Repository Takeover"
date: 2026-06-04 15:15:26 +0000
categories: [Daily Signal]
tags: [supply-chain, github, anthropic, appsec]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html
---

Researcher RyotaK (GMO) disclosed a flaw in Anthropic's Claude Code GitHub Action that allowed an attacker to take over any public repository running it by opening a single malicious GitHub issue. Because Anthropic's own action repository used the same vulnerable workflow, a working exploit could have injected malicious code into the action itself and propagated downstream to every project consuming it as a dependency. Anthropic has patched the vulnerability. Organizations using the Claude Code GitHub Action should verify they are pinned to a patched version and audit recent workflow runs for unexpected commits or permission changes.
