---
title: "Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity"
date: 2026-07-14 06:19:24 +0000
categories: [Daily Signal]
tags: [data-breach, cloud-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
---

Microsoft has mapped three distinct attack paths into corporate Salesforce environments used over the past year by actors whose methods align with the data-extortion group ShinyHunters. Notably, the attackers did not exploit a platform vulnerability in Salesforce itself — they walked in through OAuth connections that organizations had already extended to trust third-party apps and vendors. This trust-based access pattern is harder to detect than a traditional exploit-driven breach, since the connections themselves are legitimate and expected. Organizations using Salesforce should audit connected OAuth apps and revoke unused or overly permissive third-party integrations.
