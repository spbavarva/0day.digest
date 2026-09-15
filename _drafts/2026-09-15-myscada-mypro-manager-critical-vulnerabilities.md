---
title: "mySCADA myPRO Manager Hit by Critical Authentication Bypass Flaws"
date: 2026-09-15 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-03
---

CISA has published an advisory for mySCADA myPRO Manager versions 2.1 and
earlier, covering CVE-2026-73807 and CVE-2026-82567, rated up to CVSS 9.8.
The vulnerabilities stem from missing authorization and missing
authentication for a critical function.

Successful exploitation could let an attacker access privileged
management functions or send arbitrary SMS messages through a connected
GSM modem. Affected organizations should apply CISA's mitigations or the
vendor patch as soon as possible.
