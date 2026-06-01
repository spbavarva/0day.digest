---
title: "OpenAI Codex Authentication Tokens Stolen via codexui-android npm Supply Chain Attack"
date: 2026-06-01 09:31:15 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, openai]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
---

The `codexui-android` npm package, advertised on GitHub and npm as a remote web UI for OpenAI Codex, has been identified as malicious — it steals authentication tokens from developer machines. The package accumulated over 29,000 weekly downloads and remained available on npm as of the time of reporting.

Any developer who installed `codexui-android` should immediately revoke their OpenAI API keys and any Codex authentication tokens accessible from the affected machine. Check for secondary payloads or persistence mechanisms. The package's credible branding and high download count suggest a significant number of developers may be affected.
