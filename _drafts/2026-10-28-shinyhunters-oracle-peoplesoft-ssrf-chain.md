---
title: "ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws"
date: 2026-10-28 06:04:58 +0000
categories: [Daily Signal]
tags: [ssrf, zero-day, cve, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html
---

The critical Oracle PeopleSoft vulnerability that the ShinyHunters group has
exploited since May turned out to be three flaws chained together, not a
single bug, according to researchers who disclosed the chain this week.
Oracle patched all three under one identifier, CVE-2026-35273, back in June.

The root cause is a server-side request forgery that reaches an internal
management interface, because PeopleSoft trusts requests originating from
its own loopback address.

Organizations running Oracle PeopleSoft should confirm the June patch for
CVE-2026-35273 is applied, given confirmed exploitation dating back to May.
