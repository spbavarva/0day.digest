---
title: "CISA Issues Five Rockwell Automation ICS Advisories, Including Critical CVSS 9.4 Auth Bypass"
date: 2026-06-16 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, ics]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-167-05
---

CISA published five advisories on June 16 covering Rockwell Automation industrial control products. The most severe affects FLEX I/O EtherNet/IP Adapters (1794-AENTR/AENTRXT v2.012): CVE-2026-0646 and CVE-2026-0647 (CVSS 9.4) allow unauthorized access and account takeover via missing authentication for a critical function. Additional advisories cover CompactLogix and ControlLogix 5570/5370 controllers (CVE-2026-11317, CVSS 7.5, DoS causing major nonrecoverable fault in critical manufacturing and energy sectors), RSLinx Classic (CVE-2020-13573, CVSS 7.5, DoS), FactoryTalk Analytics PavilionX (CVE-2025-14272, CVSS 7.0, missing authorization enabling privileged operations), and CompactLogix 5370 (additional DoS conditions). Affected sectors include critical manufacturing, energy, food and agriculture, and water. Asset owners should apply Rockwell-provided patches immediately and ensure affected OT devices are not directly internet-exposed.
