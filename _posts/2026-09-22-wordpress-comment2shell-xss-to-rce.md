---
title: "WordPress 'Comment2Shell' Flaw Turns Anonymous Comment XSS Into Admin RCE"
date: 2026-09-22 06:03:14 +0000
categories: [Daily Signal]
tags: [xss, rce, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
---

A flaw in WordPress core let an anonymous visitor leave a comment that
planted a hidden script on the page. If a logged-in administrator later
opened that page, the script could run code on the site's server.

WordPress fixed the flaw, tracked as CVE-2026-93485 and called
"Comment2Shell," on September 17 in version 7.1.1, and told site owners to
update right away.
