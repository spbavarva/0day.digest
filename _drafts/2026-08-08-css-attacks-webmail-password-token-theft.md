---
title: "New CSS-Based Attacks Break Webmail Isolation to Steal Passwords and Tokens"
date: 2026-08-08 08:03:57 +0000
categories: [Daily Signal]
tags: [xss, appsec, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
---

New research from a PortSwigger researcher shows that content embedded in
an email can escape its message boundary and interfere with the
surrounding webmail interface using CSS. Attack chains were demonstrated
across Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and AOL Mail.
Depending on the target, the techniques can capture passwords and tokens,
hijack trusted UI actions, take over connected third-party accounts, or
manipulate AI tools that read email content. Because the flaws span
multiple independently-run webmail providers, patch status and timelines
will vary by provider.
