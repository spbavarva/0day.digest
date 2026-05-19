---
title: "ScadaBR 1.2.0 Hit by Four CVEs Including Unauthenticated RCE (CVSS 9.1)"
date: 2026-05-19 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce, ics]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-03
---

CISA issued an advisory for ScadaBR 1.2.0 covering four CVEs (CVE-2026-8602 through CVE-2026-8605) with a combined CVSS score of 9.1.
Vulnerabilities include missing authentication for critical functions, OS command injection, CSRF, and hardcoded credentials — all exploitable for unauthenticated remote code execution.
ScadaBR is a widely used open-source SCADA/HMI platform deployed in critical infrastructure sectors.
Operators should apply available mitigations, restrict network access to ScadaBR instances, and monitor for unauthorized access or unexpected process changes.
