---
title: "NIST Narrows NVD Enrichment to CISA KEV and Critical Software CVEs"
date: 2026-04-16 10:47:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/nist-prioritizes-nvd-enrichment-for-cves-in-cisa-kev-critical-software/
---

NIST has announced that, to manage the growing volume of CVE submissions, NVD enrichment
will no longer be applied automatically to all entries. Only CVEs that appear in the CISA
Known Exploited Vulnerabilities (KEV) catalog or that affect software meeting specific
criticality criteria will receive full enrichment — including CVSS scores, CWE mappings,
and CPE data.

This is a significant operational change for vulnerability management programs that rely on
NVD as the authoritative enrichment source. Tooling that pulls CVSS scores or CPE data
from NVD for triage automation may silently return incomplete results for lower-priority
CVEs that fall outside the enrichment criteria.

Security teams should audit their vuln management pipeline's NVD dependency and consider
supplementing with additional enrichment sources — such as OSV, vendor advisories, or
commercial intel feeds — to maintain full coverage for CVEs outside the NIST priority set.
