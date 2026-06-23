---
title: "Squidbleed: 29-Year-Old Squid Proxy Bug Can Leak Cleartext HTTP Requests"
date: 2026-06-22 14:29:46 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, appsec, anthropic]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html
  - name: SecurityWeek
    url: https://www.securityweek.com/decades-old-squid-proxy-flaw-squidbleed-can-expose-user-data/
---

Researchers at Calif.io disclosed Squidbleed, a heap over-read in the Squid web proxy that can leak another user's cleartext HTTP request — including any credentials or session tokens it carries — to anyone already permitted to send traffic through the same proxy. The bug traces back to a 1997 FTP-parsing change and is still live in Squid's default configuration. SecurityWeek reported the flaw was found with the aid of Claude's Mythos Preview model and described it as Heartbleed-style. Operators running Squid in shared-proxy configurations should check for patches and review who else's traffic could be exposed.
