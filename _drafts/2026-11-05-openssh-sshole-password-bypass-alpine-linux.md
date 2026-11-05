---
title: "OpenSSH Issues Emergency Fix for '*sshole' Flaw Letting Long Passwords Bypass Auth"
date: 2026-11-05 16:42:46 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html
---

A newly disclosed OpenSSH vulnerability, dubbed "*sshole," lets attackers
log in to certain Alpine Linux and other musl-based systems configured to
block password authentication, by submitting an oversized password between
257 and 1,024 bytes. Exploitation requires only network access, a valid
account name, and an overlong password string.

OpenSSH rates the flaw critical and released version 10.6p2 to fix it;
Alpine has published updated packages. Admins running musl-based Linux
systems with SSH key-only authentication should patch immediately.
