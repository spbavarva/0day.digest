---
title: "Microsoft Defender's Own Driver Can Be Weaponized to Delete Security Software at Boot"
date: 2026-08-21 15:52:10 +0000
categories: [Daily Signal]
tags: [vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html
---

Check Point Research disclosed a technique that abuses Microsoft Defender's
own legitimately signed boot-time remediation driver, BTR.sys (Boot Time
Removal Tool), to perform arbitrary kernel-level file and registry
operations. It affects Windows 7 through Windows 11 25H2. No software flaw
is exploited and no external driver is imported — the attack relies purely
on the driver's intended capabilities, making it hard to distinguish from
legitimate Defender activity.
