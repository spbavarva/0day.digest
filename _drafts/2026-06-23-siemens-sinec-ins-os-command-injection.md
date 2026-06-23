---
title: "Siemens SINEC INS Vulnerable to OS Command Injection and Path Traversal"
date: 2026-06-23 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-04
---

CISA published an advisory detailing multiple vulnerabilities in Siemens
SINEC INS versions before V1.0 SP2 Update 6, including an OS command
injection flaw rated CVSS v3 8.8, alongside path traversal, execution with
unnecessary privileges, and use of a predictable salt in a one-way hash.
Siemens has released a new version that addresses the issues. Operators
running SINEC INS should update to the patched release.
