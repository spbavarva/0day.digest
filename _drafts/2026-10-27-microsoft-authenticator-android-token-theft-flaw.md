---
title: "Microsoft Authenticator Flaw Let Unprivileged Android Apps Steal Work Account Tokens"
date: 2026-10-27 12:09:50 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/microsoft-authenticator-flaw-let.html
---

Microsoft fixed a flaw, tracked as CVE-2026-80097, in its Authenticator
app for Android that let a malicious app with no special permissions
impersonate a trusted Microsoft app, such as Teams. By posing as a
trusted app, the malicious app could collect sign-in tokens tied to a
victim's work account.

The fix shipped in Authenticator for Android version 6.2606.4246. Anyone
using Microsoft Authenticator on Android should confirm they're running
the patched version.
