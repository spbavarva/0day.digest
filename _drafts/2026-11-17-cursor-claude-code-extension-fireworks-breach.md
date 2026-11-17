---
title: "Cursor Traces Malicious Claude Code Extension to Compromised Fireworks API Key"
date: 2026-11-17 18:38:37 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach, anthropic]
severity: critical
must_know: true
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/application-security/cursor-malicious-claude-code-extension-third-party-breach
---

Cursor says a compromised API key issued to AI infrastructure provider
Fireworks was used by threat actors to access Cursor data and credentials,
after a malicious Claude Code extension was traced back to the breach. The
attackers didn't breach Cursor directly — they used a stolen Fireworks key
to reach Cursor's systems.

Organizations using Cursor or Fireworks-backed integrations should review
and rotate any credentials shared with these services and watch for
unauthorized Claude Code extensions pulled from unofficial or compromised
sources.
