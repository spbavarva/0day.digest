---
title: "CISA Advisory: XCharge C6 EV Charger Flaws Allow RCE and Admin Takeover (CVSS 9.8)"
date: 2026-05-28 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce]
severity: high
must_know: false
sources:
  - name: CISA
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-08
---

CISA advisory ICSA-26-148-08 covers critical vulnerabilities (CVSS 9.8) in the
XCharge C6 electric vehicle charger. Flaws include downloading code without
integrity verification, a stack-based buffer overflow, and insecure default
initialization. Successful exploitation gives an attacker administrator access
or arbitrary code execution on the charging device. XCharge C6 units are deployed
worldwide in transportation infrastructure. Operators should apply available
patches and segment EV charging networks from IT environments to limit blast
radius if a charger is compromised.
