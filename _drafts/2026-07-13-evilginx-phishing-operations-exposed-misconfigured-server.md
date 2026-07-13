---
title: "Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365"
date: 2026-07-13 07:30:00 +0000
categories: [Daily Signal]
tags: [phishing]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
---

French security firm Lexfo uncovered three live Evilginx-based Microsoft
365 phishing operations after finding a misconfigured attacker server.
The operator had left a Python web server (`python3 -m http.server 8080`)
running with directory listing enabled, and the launch command was still
visible in a readable `.bash_history` file. That single operational
security lapse let researchers pull the operator's entire toolkit and
pivot to two additional related phishing operations.
