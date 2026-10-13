---
title: "Two Critical MarkLogic Flaws Allow Persistent Admin Takeover"
date: 2026-10-13 08:44:01 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html
---

Progress Software disclosed 31 new flaws in MarkLogic Server, scoring five
as critical. Two of them could let an account with only limited delegated
management privileges escalate to full administrator control of the
server.

Fixes have been available since September 10 in MarkLogic 11.3.7 and
12.1.0. Deployments using delegated management roles should patch and
audit existing privilege grants.
