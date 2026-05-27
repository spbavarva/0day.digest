---
title: "CVSS 9.8 Hard-Coded Password in Eppendorf BioFlo 320 Bioreactor Grants Full Device Access"
date: 2026-05-26 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-146-01
---

CISA has published a medical ICS advisory for CVE-2026-7251, a hard-coded password vulnerability affecting all versions of the Eppendorf BioFlo 320 bioreactor. The flaw carries a CVSS v3 score of 9.8 and grants an attacker full access to the device's functionality and data.

Hard-coded credentials cannot be patched by users through configuration changes alone. The BioFlo 320 is deployed in healthcare and biotech environments worldwide. Organizations using this device should contact Eppendorf for vendor guidance, isolate the bioreactor from untrusted network segments, and restrict physical access pending a firmware fix.
