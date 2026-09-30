---
title: "OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory"
date: 2026-09-30 08:09:28 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html
---

OpenSSL patched a high-severity flaw in its DTLS implementation that can leak
unencrypted heap memory to the other side of a connection, or crash the
affected program. DTLS is the TLS variant used for UDP traffic.

The bug triggers when a handshake retransmission begins while a larger
handshake message is still being reassembled. Given OpenSSL's ubiquity, any
service terminating DTLS (VPNs, WebRTC, some IoT protocols) should prioritize
this update.
