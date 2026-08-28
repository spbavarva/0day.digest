---
title: "Android 17 Adds OS-Wide Encrypted Client Hello to Block Network Eavesdropping"
date: 2026-08-28 16:20:46 +0000
categories: [Daily Signal]
tags: [google, appsec]
severity: informational
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html
---

Google announced new network security protections in Android 17, including
OS-wide support for Encrypted Client Hello (ECH), a privacy standard that
prevents networks from seeing which websites a user visits during the TLS
handshake. The update also addresses cellular network vulnerabilities and
adds safeguards for home network privacy. Making ECH support system-wide,
rather than leaving it to individual apps or browsers, closes a gap that
let network operators observe destination hostnames even over otherwise
encrypted connections.
