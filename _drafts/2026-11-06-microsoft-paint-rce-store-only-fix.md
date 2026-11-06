---
title: "Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It"
date: 2026-11-06 12:06:43 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html
---

CVE-2026-83844, an out-of-bounds read vulnerability in Windows Paint that
could let an attacker run code over a network, now has a fix — but it
ships only through a Microsoft Store update (build 11.2609.401.0), not
through standard Windows Update.

Because many organizations manage patching through Windows Update alone,
this fix can be easily missed. Admins should verify Paint's Store update
channel is reachable and confirm the installed build number directly
rather than relying on normal patch compliance reporting.
