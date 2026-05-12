---
title: "CISA Advisory: ABB AC500 V3 PLC Stack Buffer Overflow Rated CVSS 9.8 Enables RCE"
date: 2026-05-12 12:00:00 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, ics]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-05
---

CISA published an advisory for a stack buffer overflow in ABB AC500 V3 PLCs rated CVSS
9.8, affecting versions PM5xxx 3.9.0 and 3.9.0_HF1. An attacker who exploits this
vulnerability could crash the device, cause denial-of-service, or potentially achieve
remote code execution. ABB released a firmware update that resolves the flaw. AC500 V3
PLCs are used in industrial automation across critical manufacturing environments
worldwide. OT/ICS teams should apply the ABB firmware update and review whether affected
PLCs are accessible from untrusted network segments, implementing additional firewall
rules if patching cannot be completed immediately.
