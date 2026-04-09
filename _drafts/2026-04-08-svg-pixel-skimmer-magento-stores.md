---
title: "SVG Pixel Trick Hides Credit Card Skimmer Across Nearly 100 Magento Stores"
date: 2026-04-08 22:34:26 +0000
categories: [Daily Signal]
tags: [malware, appsec, data-breach]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-use-pixel-large-svg-trick-to-hide-credit-card-stealer/
---

Attackers are concealing credit card skimming code inside a 1×1 pixel SVG image embedded in Magento store pages. File-content scanners that don't parse SVG internals miss the payload entirely. The campaign has compromised nearly 100 online stores.

This is an evolution of classic Magecart injection — moving from JavaScript files and inline scripts to image assets as the carrier. E-commerce operators should audit all SVG assets for embedded scripts, review Content Security Policy headers to block exfiltration to unknown domains, and monitor for unexpected outbound requests from checkout pages.
