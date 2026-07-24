---
title: "Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers"
date: 2026-07-24 11:45:17 +0000
categories: [Daily Signal]
tags: [microsoft, rce, cve, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
---

A crafted SVG submitted to Bing's image search executed commands as
NT AUTHORITY\SYSTEM on Microsoft's production image-processing workers,
and as root on the Linux machines in the same fleet, according to
researchers at XBOW. The result was reproducible across different hosts
and network ranges, indicating the flaw sat in Bing's image-processing
tier rather than one misconfigured machine. Microsoft assigned critical
CVEs, including CVE-2026-32194, and has fixed the issue.
