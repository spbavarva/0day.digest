---
title: "PamStealer Uses Fake Maccy Sites to Steal Mac Login Passwords"
date: 2026-07-03 08:03:37 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
---

Jamf Threat Labs identified PamStealer, a new macOS information stealer
distributed as a compiled AppleScript (.scpt) file impersonating Maccy, a
legitimate open-source clipboard manager. The malware uses PAM checks as
part of its infection process to siphon sensitive data from infected
Macs. Users should only install Maccy and similar utilities from official
sources — Homebrew, the Mac App Store, or verified GitHub releases — and
treat unsigned .scpt downloads impersonating known open-source tools as
a red flag.
