---
title: "EVoke EV Charging Station Software Has Critical Missing-Authentication Flaw"
date: 2026-06-25 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, ics, iam]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-176-02
---

CISA disclosed multiple vulnerabilities (CVSS 9.4) in EVoke Systems'
Charging Station Management System (CSMS), affecting all versions. The
flaws include missing authentication for critical functions, insufficient
restriction of authentication attempts, and weak session expiration.
Successful exploitation could let an attacker gain unauthorized
administrative control over EV charging stations or disrupt charging
service through denial-of-service. The advisory does not list a patched
version, so operators should review CISA's mitigation guidance directly.
