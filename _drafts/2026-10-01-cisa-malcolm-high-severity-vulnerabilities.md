---
title: "CISA Discloses High-Severity Flaws in Its Own Malcolm Network Analysis Tool"
date: 2026-10-01 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, xss, ssrf]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-254-01
---

CISA has disclosed multiple vulnerabilities in its own open-source network
traffic analysis tool, Malcolm, with a combined CVSS score of 8.8.

The flaw set spans cross-site scripting, OS command injection, path
traversal, server-side request forgery, authentication bypass by spoofing,
missing authorization, and use of default credentials.

Organizations running Malcolm should check for an available patched
release and review deployments for default credentials.
