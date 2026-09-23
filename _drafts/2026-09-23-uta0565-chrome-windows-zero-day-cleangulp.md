---
title: "Chinese Hackers Chain Chrome-Windows Zero-Days to Deploy CLEANGULP Malware"
date: 2026-09-23 08:29:24 +0000
categories: [Daily Signal]
tags: [zero-day, rce, malware, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html
---

A Chinese threat actor tracked as UTA0565 exploited a Chrome-Windows
zero-day chain in the wild, using fake websites to deliver CLEANGULP
malware. The attacks were detected on September 3 and 4, 2026.

The chain combines two Chrome vulnerabilities (CVE-2026-85046,
CVE-2026-87491) with a flaw in the Windows Advanced Local Procedure
Call component (CVE-2026-85880) to break out of the browser sandbox.
Ensure Chrome and Windows are fully patched.
