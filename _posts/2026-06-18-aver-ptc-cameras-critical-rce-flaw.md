---
title: "Critical Flaw in AVer PTC Cameras (CVSS 9.8) Allows Arbitrary Code Execution"
date: 2026-06-18 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce]
severity: critical
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-169-01
---

CISA disclosed a critical vulnerability (CVE-2026-40624, CVSS v3 9.8)
affecting AVer PTC500S, PTC115, PTC500+, and PTC115+ pan-tilt cameras,
caused by files or directories being accessible to external parties.
Successful exploitation could allow arbitrary code execution. The
affected cameras are deployed worldwide across government, commercial,
and healthcare facilities. Operators should restrict network exposure of
these devices and apply vendor remediation once available.
