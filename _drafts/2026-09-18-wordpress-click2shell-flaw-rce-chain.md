---
title: "New WordPress Click2Shell Flaw Chains to Remote Code Execution"
date: 2026-09-18 16:56:19 +0000
categories: [Daily Signal]
tags: [rce, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html
---

WordPress patched a set of core vulnerabilities, one of which lets a
crafted web link — opened by a logged-in administrator — silently install
a theme from the official WordPress.org directory without any click to
confirm. Security firm pwn.ai, which reported the flaw, calls the attack
chain Click2Shell; on its own the flaw only forces a theme install, but it
can be chained further toward code execution.
