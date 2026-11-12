---
title: "Node.js Patches 16 Flaws Including HTTP/2 Crash and Data Leak Bugs"
date: 2026-11-12 08:20:37 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html
---

Node.js fixed 16 flaws this week, including two HTTP/2 bugs in its
built-in HTTP/2 support. One lets unauthenticated clients crash servers on
the 24.x and 26.x release lines; the other can cause a server to leak
pieces of memory, including response data meant for other connections.

Fixed versions are available for all three supported lines: 22.23.5,
24.22.3, and 26.13.1. Anyone running a Node.js HTTP/2 server should
upgrade.
