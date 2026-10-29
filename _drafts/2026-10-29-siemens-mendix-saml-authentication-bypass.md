---
title: "Siemens Mendix SAML Module Vulnerable to Authentication Bypass"
date: 2026-10-29 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, iam]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-302-01
---

The Mendix SAML module contains an authentication bypass flaw
(CVE-2026-89209) that could let an unauthenticated remote attacker gain
unauthorized access by replaying a valid SAML assertion in IdP-initiated
authentication flows. Siemens has released updated versions for the
Mendix 9, 10, and 11-compatible SAML modules; affected organizations should
update immediately.
