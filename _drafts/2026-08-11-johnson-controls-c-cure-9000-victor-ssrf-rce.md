---
title: "Johnson Controls C-CURE 9000 and Victor Application Server Vulnerable to SSRF, RCE"
date: 2026-08-11 12:00:00 +0000
categories: [Daily Signal]
tags: [ssrf, rce, cve, ics]
severity: critical
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-01
---

CISA published an advisory (Update A) for Johnson Controls C-CURE 9000
and Victor application server, warning that successful exploitation could
let a network-adjacent attacker achieve remote code execution. Affected
versions include C-CURE 9000 <=v3.10.1 and Victor Application Server
<=v4.10 (CVE-2026-21655, CVSS 9.6), plus Victor Web <=v7.1
(CVE-2026-34496). Organizations running these physical access control
platforms should apply vendor patches per the CISA advisory.
