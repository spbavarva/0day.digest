---
title: "108 Malicious Chrome Extensions Share C2 Infrastructure to Steal Google and Telegram Data"
date: 2026-04-14 08:35:00 +0000
categories: [Daily Signal]
tags: [malware, appsec, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html
---

Researchers at Socket identified a coordinated cluster of 108 malicious Chrome extensions all
communicating with the same C2 infrastructure. The extensions collectively steal Google and
Telegram credentials, inject ads into web pages, and execute arbitrary JavaScript in the
browser context of every site visited.

The campaign has affected an estimated 20,000 users. The shared C2 backend suggests a single
threat actor operating at scale through the Chrome Web Store.

Users should audit installed Chrome extensions, removing any that were not explicitly installed
or that have recently appeared in the store. Enterprise security teams should enforce extension
allowlisting where possible and scan deployed Chrome instances for the identified extensions.
