---
title: "New cPanel Flaw Lets a Hosting Account Run Code as Root"
date: 2026-09-23 12:16:00 +0000
categories: [Daily Signal]
tags: [rce, privilege-escalation, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html
---

A flaw in cPanel's CalDAV and CardDAV service lets any hosting
account holder run code as root and take full control of the server,
cPanel disclosed. A second bug in the WP Toolkit plugin, used to
manage WordPress installs, allows an account holder to modify
databases belonging to other accounts on the same server.

cPanel has released fixed versions for both issues. Hosting providers
running cPanel should apply the updates promptly given the
root-level impact of the CalDAV/CardDAV flaw.
