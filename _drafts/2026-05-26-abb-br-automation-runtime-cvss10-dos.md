---
title: "CVSS 10.0 DoS in ABB B&R Automation Runtime Threatens Critical Industrial Infrastructure"
date: 2026-05-26 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-146-04
---

CISA has issued an ICS advisory for a denial-of-service vulnerability in the ABB B&R Automation Runtime System Diagnostics Manager (SDM), scoring a maximum CVSS 10.0. Affected versions include Automation Runtime below 6.3 and Q4.93. Successful exploitation causes the runtime to stop, which in OT environments can halt production lines or critical industrial processes.

The flaw affects critical manufacturing, energy, and water/wastewater infrastructure globally. ABB has released an update; operators should upgrade to a fixed version immediately and segment the SDM interface from untrusted networks as a defense-in-depth measure while patching is underway.
