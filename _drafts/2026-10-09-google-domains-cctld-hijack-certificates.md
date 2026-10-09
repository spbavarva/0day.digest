---
title: "Hijacked ccTLDs Used to Obtain HTTPS Certificates for Google Domains"
date: 2026-10-09 11:43:14 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/
---

Hackers hijacked the .gh (Ghana), .sl (Sierra Leone), and .as (American
Samoa) country-code top-level domains and used that access to obtain
HTTPS certificates for several Google domains, SecurityWeek reports.

Control over ccTLD infrastructure can be enough to pass the domain-validation
checks certificate authorities use before issuing certificates, since those
checks often rely on DNS records the ccTLD operator controls.

Which specific Google domains were affected, or how the certificates were
used, wasn't detailed in available reporting. Treat ccTLD compromises as a
potential precursor to certificate-based impersonation of any domain
hosted under the affected registries.
