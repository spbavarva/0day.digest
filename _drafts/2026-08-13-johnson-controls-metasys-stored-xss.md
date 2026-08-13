---
title: "Johnson Controls Metasys Stored XSS Enables Session Hijacking (CVSS 8.0)"
date: 2026-08-13 12:00:00 +0000
categories: [Daily Signal]
tags: [xss, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-14
---

CISA disclosed CVE-2026-34491, a stored cross-site scripting flaw rated 8.0
on CVSSv3, affecting Johnson Controls Metasys versions 12 through 15.

A low-privilege user or attacker could inject a persistent malicious
payload via a crafted URL that executes in the context of other users'
sessions, including administrators, potentially leading to session
hijacking and unauthorized access to building automation systems.
