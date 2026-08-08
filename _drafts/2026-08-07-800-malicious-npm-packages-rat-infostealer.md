---
title: "Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer"
date: 2026-08-07 18:48:17 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html
---

A campaign has published nearly 800 malicious packages to the npm registry
that deliver a cross-platform remote access trojan and infostealer targeting
Windows, macOS, and Linux. Researcher Paul of OpenSourceMalware says the
packages use AI-slop-style or randomly generated typosquatting names to
blend in with legitimate packages.

Developers should audit recently added dependencies for typosquatting
patterns and verify package provenance before installing, particularly for
packages with unusually generic or auto-generated-looking names.
