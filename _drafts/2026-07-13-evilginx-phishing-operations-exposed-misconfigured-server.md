---
title: "Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365"
date: 2026-07-13 07:30:00 +0000
categories: [Daily Signal]
tags: [phishing, malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
---

French security firm Lexfo found a live Microsoft 365 Evilginx phishing operation exposed by an operator's own mistake: a Python HTTP server left running with directory listing enabled, and the launch command sitting in a readable .bash_history file. Lexfo used that exposure to pull the operator's full toolkit and pivot into two additional related phishing operations. The case is a reminder that operational security failures on the attacker side can be a valuable intelligence source for defenders.
