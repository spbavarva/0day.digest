---
title: "CISA Warns of Critical Flaws in Eufy Omni C20 and Omni X10 Pro Dashcams"
date: 2026-09-24 12:00:00 +0000
categories: [Daily Signal]
tags: [iot, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-267-02
---

CISA disclosed three vulnerabilities in Eufy's Omni C20 and Omni X10 Pro
dashcams, rated up to CVSS 9.4, affecting firmware versions below 1.6.4.

The flaws include OS command injection (CVE-2026-93289), hard-coded
credentials (CVE-2026-93290), and improper certificate validation
(CVE-2026-93291). Successful exploitation could let an attacker run
system-level commands or execute arbitrary code.

Owners should update to firmware 1.6.4 or later as soon as it's
available.
