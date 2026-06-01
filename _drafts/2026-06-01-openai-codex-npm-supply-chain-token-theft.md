---
title: "OpenAI Codex Auth Tokens Stolen via codexui-android npm Supply Chain Attack"
date: 2026-06-01 09:31:15 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, openai, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
---

A malicious npm package named codexui-android, disguised as a remote web UI for OpenAI Codex, has been stealing authentication tokens from developers. The package was advertised on GitHub and npm, accumulating over 29,000 weekly downloads before discovery. The package remains available for download at time of reporting. Developers who have installed codexui-android should treat their OpenAI API keys as compromised: rotate all keys immediately, audit API usage logs for unauthorized requests, and review connected environments for signs of lateral movement. The breadth of the package's reach — 29k weekly installs — makes this a significant supply chain event.
