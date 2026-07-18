---
title: "Unauthenticated RCE in WordPress Core (wp2shell) Now Has Public PoC"
date: 2026-07-17 21:20:10 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability, appsec]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html
---

A flaw dubbed wp2shell lets unauthenticated attackers execute code on
WordPress sites via a single HTTP request. The bug lives in WordPress core,
so a bare install with zero plugins is exploitable. Every site running
WordPress 6.9 and 7.0 was in range. The two component flaws now carry CVE
IDs, the full exploitation mechanism has been published, a related
persistent-object-cache condition has surfaced, and a working
proof-of-concept is public. Operators should patch immediately.
