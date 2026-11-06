---
title: "Malicious Browser Extensions Could Use Claude Dispatch to Run Code on Users' Computers"
date: 2026-11-06 12:06:35 +0000
categories: [Daily Signal]
tags: [anthropic, llm, rce, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html
---

Researchers at Forever Security demonstrated that a malicious browser
extension capable of running scripts on claude.ai could trigger Claude
Desktop to execute code on a user's computer. The attack relies on
Dispatch, a Claude feature that lets people send tasks from their phone to
Claude Desktop.

The researchers said the underlying flaw that enables this chain can still
be exploited. Users running Claude Desktop with Dispatch enabled should be
cautious about which browser extensions they install and watch for
Anthropic guidance on mitigations.
