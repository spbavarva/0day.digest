---
title: "Node2Shell: Researchers Demonstrate RCE in Official Node.js Builds via Brotli"
date: 2026-10-23 08:40:43 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html
---

Imperva researchers demonstrated "Node2Shell," a proof-of-concept
exploit that runs attacker-supplied code on an official, unmodified
Node.js build by feeding it crafted Brotli-compressed data.

The exploit, tracked as CVE-2026-111497, worked against Node.js
24.22.0 for Linux arm64 with no debugger or custom build required, by
targeting the bundled Brotli decoder. Applications that decompress
untrusted Brotli data should check for patched Node.js builds.
