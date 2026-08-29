---
title: "Android 17 Adds OS-Wide Encrypted Client Hello to Shield Browsing From Network Snooping"
date: 2026-08-28 16:20:46 +0000
categories: [Daily Signal]
tags: [appsec]
severity: informational
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html
---

Google has added OS-wide support for Encrypted Client Hello (ECH) in
Android 17, preventing networks from seeing which websites a device is
visiting during the TLS handshake. The update is part of a broader set of
network security protections in the release aimed at bolstering
connection privacy, addressing cellular vulnerabilities, and safeguarding
home network privacy.

ECH complements existing DNS-over-HTTPS protections by closing off one of
the last plaintext signals in a typical web connection, and applies
across the OS rather than requiring per-app support.
