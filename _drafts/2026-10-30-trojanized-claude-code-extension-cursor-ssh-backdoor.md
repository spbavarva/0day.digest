---
title: "Trojanized Claude Code Extension on Cursor Marketplace Planted SSH Backdoors"
date: 2026-10-30 14:36:54 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, anthropic]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html
---

A malicious version of Anthropic's official Claude Code VS Code extension
was distributed through Cursor's extension marketplace for approximately
11 hours on October 29, under the extension's legitimate publisher identity.

The trojanized build, version 2.1.313, installed malware designed to plant
persistent SSH backdoors on affected developer machines.

BleepingComputer estimates up to 5,000 developers may have been exposed
during the distribution window. Cursor temporarily shut down the affected
listing in response.

Developers who installed or updated the Claude Code extension around
October 29 should check for unauthorized SSH keys or backdoor persistence
and reinstall from a verified source.
