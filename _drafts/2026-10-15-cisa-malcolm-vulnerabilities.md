---
title: "CISA's Own Malcolm Network Traffic Analysis Tool Patches Multiple Vulnerabilities"
date: 2026-10-15 12:00:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, ssrf]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-280-01
---

CISA published an advisory covering vulnerabilities (CVSS up to 8.1) in
Malcolm, its own open-source network traffic analysis tool, affecting
versions through v26.08.0. The flaw set includes authentication bypass by
spoofing, incorrect authorization, server-side request forgery, CSRF, and an
alternate-path authentication bypass.

Organizations running Malcolm for network monitoring should update to the
patched release.
