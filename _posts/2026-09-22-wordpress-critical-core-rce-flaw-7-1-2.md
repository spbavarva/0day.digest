---
title: "WordPress Patches Critical Core Flaw Enabling Remote Code Execution"
date: 2026-09-22 18:03:10 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html
---

WordPress fixed a critical core flaw that lets an unauthenticated attacker
make a site load a PHP file from outside its theme folder. On some server
configurations that can escalate to full remote code execution.

The fix shipped September 22 in WordPress 7.1.2, with patches backported to
every branch the project still supports, back to 4.7. WordPress is telling
site owners to update right away.
