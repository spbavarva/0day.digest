---
title: "Researchers Claim Two RCE Exploits Bypass Telegram's New Android Widget Defenses"
date: 2026-11-17 19:34:20 +0000
categories: [Daily Signal]
tags: [rce, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/researchers-claim-two-rce-exploits-that.html
---

Security firm NebuSec says it found two remote-code-execution exploits
that bypass a security filter Telegram added to its Android app last week.
The filter was meant to restrict JavaScript execution inside bot-sent
"widgets," small interactive blocks that run code on the user's phone. The
researchers say a malicious widget can still run code outside the intended
filter boundary.

The demonstrations ran on a Telegram test server, since only approved bots
can currently send widgets in production, so real-world exploitability at
scale isn't yet confirmed. Telegram had not issued a further fix as of
this report.
