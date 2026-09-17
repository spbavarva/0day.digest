---
title: "BIND 9 Update Fixes 14 Flaws, Including Unauthenticated Crash Over DNS-over-HTTPS"
date: 2026-09-17 08:00:29 +0000
categories: [Daily Signal]
tags: [cve, vulnerability]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html
---

The Internet Systems Consortium released BIND 9.20.29 and 9.21.26,
fixing fourteen security flaws disclosed September 16 in the open-source
DNS server software. One flaw affects any BIND server that answers
DNS-over-HTTPS (DoH): a sender with no credentials can crash the `named`
process with a single request carrying an invalid signature.

The remaining flaws in the batch were not individually detailed in
available coverage. Operators running BIND 9 with DoH enabled should
prioritize this update given the pre-auth remote crash.
