---
title: "Zyxel GS1900 Patch Fails to Block Zero-Day, Switches Still Being Hacked"
date: 2026-11-05 10:56:41 +0000
categories: [Daily Signal]
tags: [zero-day, rce, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/zyxel-switch-hacks-blamed-on-patched-flaw-actually-exploited-a-zero-day/
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/zyxel-gs1900-patch-fails-to-block-zero.html
---

Researchers at Binarly found that Zyxel's earlier firmware fix for GS1900
switches, tracked as CVE-2026-107441, doesn't actually close the hole it
was meant to patch. The out-of-bounds write flaw still lets an attacker who
can reach a switch's web management interface run OS commands without
authenticating.

Zyxel has now released new firmware for 10 GS1900 models that genuinely
fixes the issue. Admins who already applied the earlier "patched" build
remain exposed and should update again immediately.
