---
title: "SAP Patches Critical Code Injection and RCE Flaws in S/4HANA and Commerce Cloud"
date: 2026-05-12 11:04:55 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-commerce-cloud-and-s-4hana/
  - name: SecurityWeek
    url: https://www.securityweek.com/sap-patches-critical-s-4hana-commerce-vulnerabilities/
---

SAP's May 2026 security patch batch addresses 15 vulnerabilities, including two critical
flaws in Commerce Cloud and S/4HANA. The Commerce Cloud flaw allows malicious code
injection leading to information disclosure; the S/4HANA vulnerability could enable code
execution. SAP ERP and e-commerce systems are frequently targeted by financially motivated
threat actors and APT groups given the sensitive business data they process. Administrators
should apply the May 2026 patches promptly, with priority on internet-facing Commerce
Cloud deployments that handle payment and order data.
