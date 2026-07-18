---
title: "OpenSSL HollowByte Flaw Let 11-Byte Requests Exhaust Server Memory"
date: 2026-07-17 20:20:53 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
---

Okta's Red Team disclosed a denial-of-service flaw in OpenSSL, named
HollowByte, where an 11-byte TLS request causes a vulnerable server to
reserve up to 131KB of memory for a message that never arrives. On glibc
systems Okta tested, that memory stays allocated until the process
restarts. OpenSSL shipped a fix in June, but with no CVE, no advisory, and
no changelog entry pointing at it — easy to miss in patch tracking.
Operators should confirm their OpenSSL build includes the June fix.
