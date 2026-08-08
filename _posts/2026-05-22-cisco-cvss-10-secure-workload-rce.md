---
title: "Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Allowing Unauthenticated Data Access"
date: 2026-05-22 05:36:18 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, cisco, cloud-security]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html
---

Cisco has patched CVE-2026-20223, a CVSS 10.0 maximum-severity vulnerability in Cisco Secure
Workload that allows an unauthenticated remote attacker to access sensitive data. The flaw arises
from insufficient validation and authentication on REST API endpoints.

No active exploitation has been reported yet, but the maximum CVSS score and unauthenticated access
vector make this a high-priority patch. Organizations running Cisco Secure Workload should apply
updates immediately and audit REST API access logs for unexpected activity.
