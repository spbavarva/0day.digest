---
title: "Malicious npm Packages Impersonate PostCSS Tools to Deliver Windows RAT"
date: 2026-06-23 08:54:32 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html
---

Researchers found a set of malicious npm packages impersonating PostCSS
tooling, including aes-decode-runner-pro, postcss-minify-selector, and
postcss-minify-selector-parser, that deliver a Windows-based remote access
trojan. The packages were published over the past month by a single npm
account and had modest download counts (145–615) before discovery.
Developers who installed packages matching these names should treat affected
systems as compromised and rotate any exposed credentials.
