---
title: "Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing"
date: 2026-10-15 12:28:13 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html
---

Next.js shipped an out-of-band security update on October 14 fixing two
critical unauthenticated remote code execution flaws, plus a high-severity
denial-of-service bug. One RCE is in React Server Components; the other is
in librsvg, the SVG-processing library Next.js pulls in via the sharp
package.

Given Next.js's widespread use in production web applications, teams should
patch promptly rather than wait for a scheduled release cycle.
