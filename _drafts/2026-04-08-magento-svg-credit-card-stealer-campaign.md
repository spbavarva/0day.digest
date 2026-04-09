---
title: "Magecart Campaign Hides Credit Card Stealer in Pixel-Sized SVG on Magento Stores"
date: 2026-04-08 22:34:26 +0000
categories: [Daily Signal]
tags: [malware, appsec, data-breach]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-use-pixel-large-svg-trick-to-hide-credit-card-stealer/
---

A Magecart campaign affecting nearly 100 Magento-powered online stores hides
payment card-stealing code inside a pixel-sized SVG image element, evading
file-based security scanners that don't inspect image content for executable
code. The technique is a novel evolution of the skimmer-concealment approaches
that have long targeted e-commerce platforms.

Magento store operators should audit all image assets and third-party JavaScript
for injected content, and consider deploying a Content Security Policy to
restrict unauthorized script execution.
