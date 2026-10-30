---
title: "Trojanized Claude Code Extension on Cursor Marketplace Installed Persistent SSH Backdoor"
date: 2026-10-30 08:55:47 +0000
categories: [Daily Signal]
tags: [supply-chain, anthropic, appsec]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html
---

A trojanized version (2.1.313) of Anthropic's official Claude Code
extension was distributed through the Cursor Marketplace, pushed out
under the extension's legitimate publisher identity as what looked
like a normal update.

The malicious update attempted to install a persistent SSH backdoor on
affected systems, giving attackers ongoing remote access to machines
that installed it. Because the update came through the official
publisher channel, users had no obvious signal to distrust it.

Anyone who updated the Claude Code extension via the Cursor
Marketplace recently should check for unexpected SSH keys or
authorized_keys entries and treat the host as potentially compromised.
