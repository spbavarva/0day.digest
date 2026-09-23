---
title: "F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE"
date: 2026-09-23 08:29:48 +0000
categories: [Daily Signal]
tags: [zero-day, rce, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
---

Attackers are exploiting a critical flaw in F5 BIG-IP Access Policy
Manager (APM) that lets them run code on a BIG-IP system without
logging in, F5 says. The flaw, CVE-2026-94127, affects only systems
in which APM serves as an OAuth authorization server, issuing access
tokens to applications.

F5 disclosed the issue on September 22 and has released engineering
hotfixes. Organizations running BIG-IP APM as an OAuth authorization
server should apply F5's hotfixes immediately given confirmed active
exploitation.
