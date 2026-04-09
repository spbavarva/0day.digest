---
title: "CISA Advisory: Contemporary Controls BASC 20T PLC Vulnerability (CVSS 9.8) Enables Full Device Control"
date: 2026-04-09 12:00:00 +0000
categories: [Daily Signal]
tags: [ics, cve, vulnerability]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-099-01
---

CISA has published an advisory for CVE-2025-13926, a critical vulnerability (CVSS 9.8) in
Contemporary Controls BASControl20 version 3.1, a programmable logic controller used in
commercial facilities and building automation systems. The flaw stems from reliance on
untrusted inputs in a security decision, enabling a remote attacker to enumerate device
components, reconfigure or rename settings, delete data, perform file transfers, and issue
remote procedure calls.

A successful exploit effectively provides unauthenticated full control over the PLC. Operators
of Contemporary Controls BASC 20T devices should apply vendor patches when available, ensure
these controllers are not directly internet-accessible, and enforce network segmentation
isolating OT devices from IT networks. Review the CISA advisory for full mitigation guidance.
