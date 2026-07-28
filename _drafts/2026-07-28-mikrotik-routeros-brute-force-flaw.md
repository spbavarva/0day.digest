---
title: "MikroTik RouterOS and Cloud Hosted Router Brute-Force Protection Flaw"
date: 2026-07-28 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-209-05
---

CISA published an advisory for CVE-2026-16347 (CVSS 8.8), an improper
restriction of excessive authentication attempts affecting all versions of
MikroTik RouterOS and Cloud Hosted Router. The flaw allows attackers to
rapidly guess passwords and gain unauthorized system access. Administrators
should apply available mitigations and enforce strong authentication
policies on exposed management interfaces.
