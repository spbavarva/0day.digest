---
title: "DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT"
date: 2026-08-04 09:03:23 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html
---

A new Russian loader-as-a-service tracked as DOUBLECUP uses ClickFix-style
lures to stage steganographic PNG images in a victim's browser cache.

The first stage drops the PNG, extracts hidden payload content from it,
and executes a second stage that delivers CountLoader and a previously
undocumented remote access trojan called DeviceManager. Defenders should
treat ClickFix-style "fix it yourself" prompts as a red flag and monitor
for unusual browser cache activity feeding into script execution.
