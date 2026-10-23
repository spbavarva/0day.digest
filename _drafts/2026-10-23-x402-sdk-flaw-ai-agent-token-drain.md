---
title: "Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents' Token Balances"
date: 2026-10-23 08:35:45 +0000
categories: [Daily Signal]
tags: [vulnerability, llm, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html
---

Security firm V12 disclosed a flaw in x402 SDKs, used by AI agents to
pay for API calls with cryptocurrency tokens, that could let a
malicious API sign a payment for an agent's entire token balance.

The root cause was the SDK's default client, which set no spending
limit until a fix added one in releases on August 18. Risk was limited
to agents that auto-sign payments and whose apps don't cap spending
themselves; agents on affected SDK versions should upgrade.
