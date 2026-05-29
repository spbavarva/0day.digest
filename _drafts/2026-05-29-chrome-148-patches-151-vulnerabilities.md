---
title: "Chrome 148 Patches 151 Vulnerabilities Including Critical-Severity RCE Bugs"
date: 2026-05-29 10:17:23 +0000
categories: [Daily Signal]
tags: [google, vulnerability, rce, cve]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/chrome-148-update-patches-151-vulnerabilities/
---

Google released Chrome 148 addressing 151 security vulnerabilities, including multiple critical-severity issues that could lead to remote code execution. No CVEs were listed as under active exploitation at time of release.

The volume of fixes is high but consistent with Chrome's rapid development cycle. Critical-severity browser RCE bugs warrant prompt patching given the browser's ubiquitous presence as an enterprise attack surface.

Administrators should push Chrome 148 updates via enterprise management tooling without waiting for user-initiated updates, prioritizing endpoints in high-risk roles (privileged users, systems with access to sensitive data).
