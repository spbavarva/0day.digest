---
title: "Critical Flaws in Grid Protection Alliance openPDC and openHistorian"
date: 2026-10-08 12:00:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability]
severity: critical
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-281-02
---

CISA has published an advisory for five vulnerabilities (CVSS up to 9.8)
in Grid Protection Alliance's openPDC and openHistorian, software used
to collect and manage phasor data in electric grid monitoring.

Affected versions include openPDC below 2.9.477/2.9.482 (including its
Docker image) and openHistorian below 2.8.580/2.8.585, covering
CVE-2026-104629, CVE-2026-100730, CVE-2026-105281, CVE-2026-85479,
CVE-2026-101022, and CVE-2026-105278. Operators running these products on
grid monitoring infrastructure should check CISA's advisory for patched
versions.
