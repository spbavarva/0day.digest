---
title: "OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted"
date: 2026-09-30 08:09:28 +0000
categories: [Daily Signal]
tags: [vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html
---

OpenSSL released fixes on September 29 for a high-severity flaw in its
DTLS implementation, the TLS variant used for UDP traffic.

DTLS resends a handshake message if no reply arrives before a timer
expires. The bug can leak heap memory to the other side of the connection,
or crash the program, when such a resend starts while a larger handshake
message is still being reassembled.
