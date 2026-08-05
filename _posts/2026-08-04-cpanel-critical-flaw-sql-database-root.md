---
title: "New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root"
date: 2026-08-04 10:36:27 +0000
categories: [Daily Signal]
tags: [cve, privilege-escalation, sqli]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html
---

cPanel patched a flaw, tracked as CVE-2026-58048 (CVSS 4.0 score: 9.4),
that let an authenticated hosting customer execute SQL in the
database's root context, crossing the boundary between a standard
cPanel account and the server's administrative database identity.

The fix shipped in a targeted security release that also closed two
other account-boundary bypass routes. Hosting providers running cPanel
should apply the update promptly given the low bar for exploitation —
any authenticated customer account.
