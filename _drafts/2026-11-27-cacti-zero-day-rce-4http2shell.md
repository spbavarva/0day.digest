---
title: "Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access"
date: 2026-11-27 05:48:20 +0000
categories: [Daily Signal]
tags: [zero-day, rce, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html
---

A new unpatched zero-day vulnerability in Cacti, an open-source network
monitoring tool, can reportedly be exploited for remote code execution
in as few as four HTTP requests using only guest-level access, according
to The Hacker News. The proof-of-concept, tracked as 4HTTP2SHELL and
4HTTP2ROOT, has not yet been assigned a CVE.

The researcher described a path from an unauthenticated HTTP session to
command execution as the Cacti server process. Organizations running
Cacti should restrict guest access and monitor for an official patch.
