---
title: "14 Trojanized npm Packages Deliver RedC2 4.0 Linux Backdoor With AI-Assisted C2"
date: 2026-08-21 18:53:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/14-trojanized-npm-packages-drop-redc2.html
---

Researchers found 14 trojanized npm packages, disguised as calendar and
streak-tracking utilities, that install RedC2 4.0 — an AI-powered Linux
backdoor. Per Trend Micro's TrendAI research (via The Hacker News), the
malicious module locates a bundled binary, marks it executable, and
launches it as a detached background process. The implant uses
AI-assisted command-and-control.

Developers who recently installed calendar or streak-tracking utilities
from npm should audit dependencies for unexpected bundled binaries and
outbound C2 traffic.
