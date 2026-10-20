---
title: "Moxa AIG-302 ThingsPro Edge Vulnerabilities Allow Sensitive Data Disclosure"
date: 2026-10-20 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-293-03
---

CISA disclosed two vulnerabilities (CVE-2026-109812, CVE-2026-109813, CVSS
v3 8.1) in Moxa's AIG-302 ThingsPro Edge firmware (versions up to 1.4.0),
including missing authorization and a hard-coded cryptographic key.

Successful exploitation could let an attacker obtain and disclose sensitive
information. Moxa gateways are deployed across critical manufacturing,
energy, and water/wastewater sectors worldwide; operators should update
firmware per vendor guidance once available.
