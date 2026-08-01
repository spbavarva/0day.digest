---
title: "Public PoC Released for Exploited Check Point SmartConsole Auth Bypass"
date: 2026-07-29 08:58:27 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, zero-day]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/rapid7-releases-poc-for-exploited-check.html
---

Rapid7 released a public proof-of-concept exploit for CVE-2026-16232, a
critical (CVSS 9.3) authentication bypass in the SmartConsole login process
on Check Point Security Management Server and Multi-Domain Security
Management Server (MDS). The flaw was already under active exploitation in
the wild before this technical detail and PoC were published. Organizations
running Check Point Security Management Server or MDS should confirm they
are on a patched build and review SmartConsole login logs for signs of prior
compromise.
