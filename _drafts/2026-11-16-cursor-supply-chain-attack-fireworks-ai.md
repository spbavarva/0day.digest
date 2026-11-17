---
title: "Cursor Supply Chain Attack Started at Fireworks AI"
date: 2026-11-16 15:45:43 +0000
categories: [Daily Signal]
tags: [supply-chain, appsec, anthropic]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks/
---

The supply chain attack that compromised Cursor originated at Fireworks
AI, where an attacker stole an access key and used it to exfiltrate
credentials. Those stolen credentials then let the attacker push malicious
copies of the Claude Code extension.

This is a textbook third-party dependency compromise: a single leaked key
at an upstream AI infrastructure provider cascaded into tampered extension
packages reaching end users. Anyone who installed Claude Code extension
updates during the affected window should treat their environment as
potentially compromised, rotate credentials, and verify extension
integrity against known-good hashes.
