---
title: "CSS: The Bomb Inside Your Inbox"
date: 2026-08-06 22:00:00 +0000
categories: [Daily Signal]
tags: [appsec, vulnerability]
severity: medium
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/css-the-bomb-inside-your-inbox
---

PortSwigger researcher Gareth Heyes demonstrated techniques for bypassing CSS
sanitization in webmail clients that render untrusted CSS inside a trusted UI.
Many webmail providers sanitize incoming CSS to prevent it from being used
maliciously, but the research shows those sanitizers can be bypassed. The
write-up focuses on the sanitization gap itself rather than a single named
vendor vulnerability. Teams building HTML/CSS sanitizers for untrusted email
content should review their allowlist logic against the bypass techniques
described.
