---
title: "SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution"
date: 2026-09-09 06:25:45 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html
---

SAP released security updates addressing multiple vulnerabilities, including
a maximum-severity flaw in SAP Extended Passport (EPP) Processing tracked as
CVE-2026-44756 (CVSS 10.0). The bug is a memory corruption issue that could
let an unauthenticated attacker fully compromise confidentiality, integrity,
and availability of affected SAP applications. It was discovered and reported
by SAP. Organizations running SAP kernel components should prioritize this
patch.
