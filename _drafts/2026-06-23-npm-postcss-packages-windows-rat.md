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

Researchers found malicious npm packages — including `aes-decode-runner-pro`,
`postcss-minify-selector`, and `postcss-minify-selector-parser` — published
under a single npm account over the past month. The packages impersonate
legitimate PostCSS tooling and are designed to deliver a Windows-based remote
access trojan to anyone who installs them. Combined downloads are in the low
hundreds, but the campaign follows the familiar supply-chain pattern:
typosquat-style naming, a plausible utility description, and a malicious
payload buried in the install. Check recent dependency installs for these
package names and audit CI pipelines that auto-install npm packages.
