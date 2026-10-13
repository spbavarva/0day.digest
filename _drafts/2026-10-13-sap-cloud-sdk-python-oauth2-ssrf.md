---
title: "SAP Discloses CVSS 10 Flaw in Cloud SDK for Python Risking OAuth2 Credential Theft"
date: 2026-10-13 17:28:50 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, ssrf, cloud-security]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-oauth2-ssrf-security-flaw/
---

SAP disclosed a maximum-severity (CVSS 10) flaw in its Cloud SDK for
Python that can cause an application to send its OAuth2 client
credentials to a server controlled by an attacker. The issue affects
multi-tenant applications on SAP Business Technology Platform that use
the SDK, and requires an attacker to control the tenant subdomain to
exploit it.

SAP addressed the flaw alongside 20 other security fixes in its October
2026 updates. Affected customers should update the SDK and rotate any
potentially exposed OAuth2 credentials.
