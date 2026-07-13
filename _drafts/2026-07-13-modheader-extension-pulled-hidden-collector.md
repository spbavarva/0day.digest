---
title: "Google and Microsoft Pull ModHeader Extension Over Hidden Data Collector"
date: 2026-07-13 17:17:24 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html
---

Google and Microsoft pulled ModHeader, a header-editing browser extension
with roughly 1.6 million installs across Chrome and Edge, after researchers
found a hidden browsing-history collector built into the official store
version. The collector was dormant, gated behind an empty allow-list that
kept it switched off, and no evidence has emerged that it ever gathered or
transmitted browsing data. The case is a reminder that widely-installed
browser extensions can silently ship data-collection code without an
obvious trigger, even in official store listings.
