---
title: "J4Care dcm4che Medical Imaging Vulnerabilities"
date: 2026-10-15 12:00:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-288-02
---

CISA disclosed four vulnerabilities (CVSS up to 9.1) in J4Care's dcm4che,
specifically the dcm4chee-arc-light medical imaging archive (version 5.35.1
and earlier). Exploitation could let an attacker delete stored medical
images, disclose patient information, inject forged studies, reassign
patient records, overwrite files, or cause denial of service.

The flaws include missing authorization and an unreachable loop-exit
condition; affected healthcare organizations should apply vendor patches.
