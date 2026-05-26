---
title: "Lazarus Group Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms"
date: 2026-05-25 09:32:54 +0000
categories: [Daily Signal]
tags: [malware, lazarus]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html
---

Fox-IT (NCC Group) disclosed RemotePE, a cross-platform, memory-only remote
access trojan attributed to North Korea's Lazarus Group. The malware targets
financial and cryptocurrency organizations via a multi-stage attack chain.

Two loaders — DPAPILoader and RemotePELoader — handle decryption and in-memory
execution, keeping the final payload off disk to evade traditional endpoint
detection. Financial and crypto firms should review EDR telemetry for
anomalous in-memory execution patterns and DPAPI decryption activity.
