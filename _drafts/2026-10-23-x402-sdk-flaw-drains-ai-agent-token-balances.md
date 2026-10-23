---
title: "Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents' Token Balances"
date: 2026-10-23 08:35:45 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, ai-safety]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html
---

Security firm V12 disclosed a flaw in the x402 SDKs, used by AI agents to
autonomously pay for API calls with tokens, that could let a malicious API
request and sign a payment for an agent's full token balance.

The root cause was the SDK's default client setting no spending limit; a
fix adding a default limit shipped on August 18. Risk was limited to
agents that automatically sign payments and whose applications hadn't set
their own limit before the fix. Teams running agents on the x402 SDK
should confirm they're on a release with the spending-limit default.
