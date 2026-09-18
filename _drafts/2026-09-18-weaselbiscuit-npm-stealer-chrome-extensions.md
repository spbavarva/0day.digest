---
title: "WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage"
date: 2026-09-18 10:40:06 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html
---

Researchers identified 13 npm packages delivering a previously
undocumented JavaScript stealer dubbed WeaselBiscuit, which harvests
data from Chrome extension storage. Per OpenSourceMalware, the malware
shares functional overlaps with BeaverTail, a strain tied to North
Korea's Contagious Interview campaign. Teams that pulled the affected
packages should audit dependencies and rotate any credentials that may
have been stored in browser extension storage.
