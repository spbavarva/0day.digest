---
title: "Public PoC Released for Actively Exploited Check Point SmartConsole Auth Bypass"
date: 2026-07-29 08:58:27 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/rapid7-releases-poc-for-exploited-check.html
---

Researchers shared additional technical detail and a public proof-of-concept
for CVE-2026-16232 (CVSS 9.3), an authentication bypass in the SmartConsole
login process for Check Point Security Management Server and Multi-Domain
Security Management Server. The flaw was already under active exploitation
before the PoC's release. Check Point has patched the vulnerability, but
organizations still running unpatched Security Management or MDS servers
should treat this as high urgency now that a public PoC exists. Review
authentication logs for anomalous SmartConsole login activity.
