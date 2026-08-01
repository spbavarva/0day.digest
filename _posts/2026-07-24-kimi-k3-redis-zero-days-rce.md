---
title: "Kimi K3 AI Agents Found Redis Zero-Days, Built RCE Exploit"
date: 2026-07-24 06:58:27 +0000
categories: [Daily Signal]
tags: [rce, zero-day, vulnerability, cve, llm]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
---

Researchers using Kimi K3 AI agents found zero-day memory flaws in Redis
and built authenticated remote-code-execution proof-of-concept exploits
against stock Redis 6.2.22, 7.4.9, 8.6.4, and 8.8.0. All four chains
require the RESTORE command; the Streams-based chains also need EVAL and
XGROUP, and the 8.8.0 chain needs EVAL plus the bundled RedisBloom module.

Redis shipped seven security releases on July 23 addressing the
underlying flaws, including 6.2.23, 7.2.15, and 7.4.10. Operators running
affected versions should patch given the public PoC exploit chains.
