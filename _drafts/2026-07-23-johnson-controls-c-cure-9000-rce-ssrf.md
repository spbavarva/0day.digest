---
title: "Johnson Controls C-CURE 9000 Flaws Allow Remote Code Execution (CVSS 9.6)"
date: 2026-07-23 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, ssrf]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-01
---

CISA advisory ICSA-26-204-01 covers critical vulnerabilities (CVSS 9.6) in
Johnson Controls C-CURE 9000 and Victor application server, affecting
C-CURE 9000/victor versions up to v2.90/v3.0 and victor Web up to v7.1. The
flaws include server-side request forgery and execution with unnecessary
privileges; successful exploitation could let an attacker with network
access achieve remote code execution. C-CURE 9000 is used as a physical
access control and security management platform. Operators should apply
available patches and restrict network access to management interfaces.
