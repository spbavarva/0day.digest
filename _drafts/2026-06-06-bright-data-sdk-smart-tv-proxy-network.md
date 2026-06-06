---
title: "Free Apps Quietly Turn Smart TVs Into Web-Scraping Proxy Nodes for AI Data Collection"
date: 2026-06-06 08:29:05 +0000
categories: [Daily Signal]
tags: [appsec, supply-chain, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
---

A researcher reverse-engineered the iOS SDK that Bright Data (formerly Luminati)
embeds in free consumer apps — including always-on smart TVs — to turn those devices
into exit nodes that relay web-scraping traffic. Bright Data markets the capability
heavily to the AI industry as part of what it calls the world's largest residential
proxy network.

Users of apps embedding this SDK become involuntary proxies without meaningful
disclosure. Security and privacy teams should audit third-party SDK inventory in
mobile and smart-device app portfolios. The arrangement carries significant regulatory
risk under GDPR and CCPA, and could expose organizations to liability if their
devices are used to scrape restricted targets.
