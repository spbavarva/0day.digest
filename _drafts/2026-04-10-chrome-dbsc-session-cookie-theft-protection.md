---
title: "Google Ships Device Bound Session Credentials in Chrome 146 to Block Cookie Theft"
date: 2026-04-10 07:58:00 +0000
categories: [Daily Signal]
tags: [google, appsec, browser-security, iam]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html
---

Google has made Device Bound Session Credentials (DBSC) generally available to all Windows
users on Chrome 146, following months in open beta. DBSC cryptographically binds session
tokens to the device's hardware, making stolen cookies useless for session hijacking even
after exfiltration.

This directly counters a core technique used by info-stealers and adversary-in-the-browser
malware, which harvest session cookies to bypass MFA. macOS support is planned for an
upcoming Chrome release. Enterprise security teams should track DBSC adoption on internal
and external web properties as the feature rolls out more broadly.
