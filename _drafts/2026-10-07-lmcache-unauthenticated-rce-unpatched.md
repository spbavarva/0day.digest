---
title: "Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely"
date: 2026-10-07 15:34:53 +0000
categories: [Daily Signal]
tags: [rce, llm, vulnerability, zero-day]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
---

A critical vulnerability in LMCache, open-source caching software used to
speed up LLM servers such as vLLM, lets an unauthenticated attacker execute
code on the cache server.

The flaw is in LMCache's multiprocess mode, where the cache runs as a
standalone server that LLM worker processes reach over the ZeroMQ messaging
library. A single network-reachable endpoint is enough to trigger remote
code execution.

No fixed version is currently available. Teams running LMCache in
multiprocess mode should restrict network access to the cache server until a
patch ships.
</content>
