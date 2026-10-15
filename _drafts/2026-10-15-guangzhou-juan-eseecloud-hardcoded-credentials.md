---
title: "Guangzhou Juan IoT Technology EseeCloud Hardcoded Credentials and IP Camera Takeover Flaws"
date: 2026-10-15 12:00:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, privilege-escalation, iot]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-288-02
---

CISA's advisory covers three vulnerabilities (CVSS up to 9.8) in Guangzhou
Juan IoT Technology's EseeCloud app and firmware (versions 4.9.6 and
4.9.86.0, respectively, and earlier). The flaws include hard-coded
credentials and improperly controlled modification of dynamically-determined
object attributes, which together could let an attacker gain control over
affected IP cameras.

Owners of EseeCloud-connected cameras should check for firmware updates and
avoid exposing camera management interfaces to the internet.
