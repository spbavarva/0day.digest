---
title: "Unauthenticated RCE Flaws Found in MZ Automation libIEC61850"
date: 2026-07-23 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06
---

CISA advisory ICSA-26-204-06 covers multiple vulnerabilities in MZ
Automation's libIEC61850 library (versions 1.0.0 through 1.6.1), including
stack-based and heap-based buffer overflows, improper handling of invalid
structures, and a NULL pointer dereference. CISA says successful
exploitation could let an unauthenticated, network-adjacent attacker crash
critical IEC 61850 services or execute arbitrary code. IEC 61850 is a widely
used protocol for substation automation and protective relaying.
Organizations using libIEC61850 should update to a patched version and
restrict network access to affected services.
