---
title: "HTTP/3 Support Lands in Burp Suite's Turbo Intruder"
date: 2026-09-23 14:00:00 +0000
categories: [Daily Signal]
tags: [appsec]
severity: informational
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/http3-in-burp-suite
---

PortSwigger added HTTP/3 support to Turbo Intruder, its high-throughput
request tool in Burp Suite. The updated tool can comfortably exceed
100,000 requests per second over Wi-Fi and auto-tunes its behavior
for HTTP/3 targets.

The release extends existing fuzzing and enumeration workflows to
HTTP/3 endpoints, which were previously untestable at the same
throughput with Turbo Intruder.
