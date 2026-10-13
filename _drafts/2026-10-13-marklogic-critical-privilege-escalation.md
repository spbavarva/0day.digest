---
title: "Two Critical MarkLogic Flaws Allow Escalation to Persistent Admin Control"
date: 2026-10-13 08:44:01 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html
---

Progress Software disclosed 31 vulnerabilities in MarkLogic Server, five
of them rated critical, including two flaws that let an account with only
limited delegated management privileges escalate to persistent
administrator control.

Fixes have been available since September 10 in MarkLogic 11.3.7 and
12.1.0. Operators running MarkLogic should confirm they're on a patched
version and review delegated-admin account privileges.
