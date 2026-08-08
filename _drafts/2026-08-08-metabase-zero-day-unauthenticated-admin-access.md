---
title: "Metabase Zero-Day Under Active Exploitation Grants Unauthenticated Admin Access"
date: 2026-08-08 06:58:31 +0000
categories: [Daily Signal]
tags: [zero-day, sqli, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html
---

Metabase has confirmed that a maximum-severity flaw (CVSS 10.0) in its
business intelligence and data visualization software is being actively
exploited in the wild as a zero-day. The bug has no assigned CVE identifier.
It allows an unauthenticated remote attacker to inject arbitrary SQL into
the Metabase application database, which can be leveraged to gain
administrative access without credentials. Organizations running
self-hosted Metabase instances should treat this as urgent, apply vendor
guidance as soon as it's available, and review logs for signs of
unauthorized admin access.
