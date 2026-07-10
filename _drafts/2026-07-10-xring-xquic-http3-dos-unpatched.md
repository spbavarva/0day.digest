---
title: "Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers"
date: 2026-07-10 11:47:43 +0000
categories: [Daily Signal]
tags: [vulnerability, zero-day]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html
---

Researcher Sebastien Fery of FoxIO disclosed an unpatched flaw, dubbed
XRING, in XQUIC, Alibaba's QUIC and HTTP/3 library. A single incorrect
variable on one line lets any remote, unauthenticated client crash a
vulnerable server using about 260 bytes of ordinary-looking QPACK
traffic, no malformed packets required. The flaw was disclosed on July 8
and remains unpatched as of this writing. Organizations running services
built on XQUIC should watch for a fix and consider rate-limiting or
filtering QUIC/HTTP/3 traffic in the meantime.
