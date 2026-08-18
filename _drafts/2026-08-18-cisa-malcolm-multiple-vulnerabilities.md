---
title: "CISA Discloses Multiple Vulnerabilities in Malcolm Network Traffic Analysis Tool"
date: 2026-08-18 12:00:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, rce]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-230-01
---

CISA disclosed multiple vulnerabilities in Malcolm, an open-source network
traffic analysis tool, tracked as CVE-2026-55676, CVE-2026-63133,
CVE-2026-63134, CVE-2026-63177, CVE-2026-19670, and CVE-2026-19671. The
flaws include unrestricted resource allocation, path traversal, and
unrestricted file upload, with a top CVSS v3 score of 8.8.

Successful exploitation could let an attacker cause a denial-of-service
condition or execute arbitrary code. Affected versions are Malcolm
<26.06.1, <26.07.0, and <=26.07.1; users should update to a patched
release.
