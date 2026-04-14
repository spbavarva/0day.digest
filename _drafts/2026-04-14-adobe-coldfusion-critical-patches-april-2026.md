---
title: "Adobe Patches 55 Vulnerabilities Across 11 Products; ColdFusion and Reader at Highest Risk"
date: 2026-04-14 16:48:03 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/adobe-patches-55-vulnerabilities-across-11-products/
---

Adobe has patched 55 security vulnerabilities across 11 products as part of April 2026 Patch
Tuesday. Adobe ColdFusion carries the highest exploitation risk among the affected products,
with critical flaws that could enable remote code execution. Adobe Reader also received an
emergency patch for an actively exploited RCE flaw that is confirmed in CISA's KEV catalog.

ColdFusion has a documented history of rapid weaponization: functional exploits have appeared
within hours of patch release in prior cycles. Any internet-facing ColdFusion instance should
be patched immediately or isolated from the network until patching is complete.

Organizations running ColdFusion should apply patches without waiting for a change window and
consider placing instances behind a WAF with ColdFusion-specific rule sets. Adobe Reader
patches should be treated as emergency updates given the confirmed active exploitation.
