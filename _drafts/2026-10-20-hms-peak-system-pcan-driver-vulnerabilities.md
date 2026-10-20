---
title: "HMS Networks PEAK-System PCAN Windows Drivers Vulnerable to Kernel Crash"
date: 2026-10-20 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: medium
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-293-01
---

CISA detailed five vulnerabilities (CVSS v3 7.1) in HMS Networks'
PEAK-System Device Driver Setup and PCAN Windows CAN device drivers,
affecting versions up to 5.1.2.1151 and 5.1.2 respectively.

Successful exploitation could crash the Windows kernel. CAN bus drivers are
widely used in industrial and automotive diagnostic tooling; affected users
should update to patched driver versions once available.
