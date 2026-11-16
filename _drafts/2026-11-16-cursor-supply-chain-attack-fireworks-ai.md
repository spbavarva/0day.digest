---
title: "Cursor Supply Chain Attack Started at Fireworks AI"
date: 2026-11-16 15:45:43 +0000
categories: [Daily Signal]
tags: [supply-chain, anthropic, llm]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks/
---

An attacker compromised Fireworks AI by stealing an access key, then used it
to exfiltrate credentials. Those stolen credentials enabled the attacker to
push malicious copies of the Claude Code extension through Cursor's
distribution channel.

Developers who installed extension updates during the compromise window may
have received a tampered build. This is a software supply chain attack on AI
coding tool distribution infrastructure, not a vulnerability in Claude Code
itself.
