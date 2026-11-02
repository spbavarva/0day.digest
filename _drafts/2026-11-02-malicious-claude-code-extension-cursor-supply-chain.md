---
title: "Malicious Claude Code Extension Served to Cursor Users in Supply Chain Attack"
date: 2026-11-02 11:29:39 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, anthropic]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/
---

A malicious extension impersonating a Claude Code integration was
distributed to Cursor users in a supply chain attack. Once installed,
it performed host reconnaissance and attempted to establish a reverse
SSH tunnel back to attacker infrastructure.

The incident is a compromise of a third-party extension distributed
through Cursor, not a compromise of Anthropic's own Claude Code
product. Developers using Cursor or similar AI coding tools should
audit installed extensions and their sources.
