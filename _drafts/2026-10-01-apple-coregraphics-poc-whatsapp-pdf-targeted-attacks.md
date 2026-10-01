---
title: "Apple CoreGraphics Flaw Gets Public PoC, WhatsApp PDF Checks Hint at Delivery Path"
date: 2026-10-01 05:54:41 +0000
categories: [Daily Signal]
tags: [zero-day, cve, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
---

Security researchers published the first public proof-of-concept for
CVE-2026-86950, an Apple CoreGraphics flaw Apple says may have been used in
attacks against specific targeted individuals. The PoC uses a malicious PDF
with a crafted embedded font to crash unpatched iPhones and Macs; the public
code triggers a crash rather than full code execution. WhatsApp's PDF
handling checks are cited as a possible delivery path, though this has not
been confirmed as an active attack vector. Users should apply Apple's
available patches.
