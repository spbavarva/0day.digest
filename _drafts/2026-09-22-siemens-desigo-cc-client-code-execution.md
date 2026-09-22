---
title: "Siemens Desigo CC Client Code Execution Flaw via Malicious Graphics Files"
date: 2026-09-22 12:00:00 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-265-05
---

A Client Code Execution vulnerability in the Siemens Desigo CC family (V6)
lets attackers run arbitrary code on client devices through specially
crafted graphics documents containing embedded scripts.

The malicious scripts execute when opened in the client application,
potentially compromising the client operating system and enabling lateral
movement within the organization. Siemens has released fixes for affected
products.
