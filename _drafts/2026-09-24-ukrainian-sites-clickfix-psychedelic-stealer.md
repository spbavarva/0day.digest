---
title: "Hacked Ukrainian Sites Serve Fake Cloudflare ClickFix Lures for New Psychedelic Stealer"
date: 2026-09-24 14:29:06 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html
---

An active ClickFix campaign is compromising legitimate Ukrainian business
websites to inject fake Cloudflare verification pages, tricking visitors
into installing a previously undocumented information stealer dubbed
Psychedelic.

When a visitor interacts with the bogus verification page, the lure
copies a Windows Installer command to the clipboard and instructs them to
paste and run it — a classic ClickFix social-engineering pattern that
requires no exploit.

Site operators should audit for injected verification-page content, and
users should be trained never to paste and run commands prompted by a web
page.
