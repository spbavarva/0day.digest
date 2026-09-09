---
title: "New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root"
date: 2026-09-09 08:19:32 +0000
categories: [Daily Signal]
tags: [privilege-escalation, rce, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html
---

cPanel has patched a flaw that lets a hosting account with mail-related
privileges take over an entire server. An authenticated account holder can
create arbitrary files through the EmailTrack feature and use them to run
code as root. cPanel published the advisory on September 8 and says every
supported version of cPanel and WHM is affected. Hosting providers should
apply the update promptly given the low bar for authentication.
