---
title: "Study of 85 Crypto Wallet Extensions Finds Address Leaks and Tracking Risks"
date: 2026-07-14 11:55:00 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: informational
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html
---

Researchers at KU Leuven tested 85 of the most popular cryptocurrency wallet browser extensions and found that many leak enough information to link and track users across sites. The way these wallets communicate with websites and blockchain nodes can tie a user's separate wallet addresses together, and combined with identifying information already present on a site, can enable outside tracking of activity across the web. The findings point to a systemic privacy weakness in how wallet extensions handle cross-site communication rather than a single exploitable bug. Wallet developers should review dApp-communication flows for unnecessary address or fingerprint exposure.
