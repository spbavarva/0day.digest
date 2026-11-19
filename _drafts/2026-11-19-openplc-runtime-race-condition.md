---
title: "Autonomy Logic OpenPLC Runtime Flaw Allows Unauthenticated Admin Account Creation"
date: 2026-11-19 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: medium
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01
---

CISA warned of a race condition vulnerability (CVE-2026-126088, CVSS 8.1)
in Autonomy Logic OpenPLC Runtime, open-source PLC software used in
critical manufacturing, energy, transportation, and water sector
environments. Successful exploitation could allow several unauthenticated
admin accounts to be created on affected systems. Versions up to 4.2.4
are affected. No active exploitation reported; patch per CISA guidance.
