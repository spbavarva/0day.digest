---
title: "PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords"
date: 2026-07-03 08:03:37 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
---

Jamf Threat Labs identified a new macOS information stealer dubbed
PamStealer. It's distributed as a compiled AppleScript (.scpt) file
impersonating Maccy, a legitimate open-source clipboard manager. The malware
uses PAM (Pluggable Authentication Module) checks as part of its infection
tricks to siphon login credentials and other sensitive data from infected
Macs. Users should verify that clipboard utilities and similar tools are
downloaded only from official sources.
