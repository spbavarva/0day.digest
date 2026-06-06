---
title: "Free Apps Secretly Enroll Smart TVs as Exit Nodes in Bright Data's AI Scraping Proxy Network"
date: 2026-06-06 08:29:05 +0000
categories: [Daily Signal]
tags: [supply-chain, appsec, llm]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
---

Researchers reverse-engineered the iOS SDK Bright Data (formerly Luminati) embeds in consumer apps, documenting how it silently enrolls user devices — including always-on smart TVs — as exit nodes in a residential proxy network. Bright Data markets the network heavily to AI companies for web scraping. Users of affected apps are unknowingly relaying third-party traffic. Bright Data claims to operate the world's largest residential proxy network; AI demand for residential IPs to bypass scraping blocks is the commercial driver. App reviewers and enterprise mobile security teams should flag SDKs that request broad network permissions without clear user disclosure.
