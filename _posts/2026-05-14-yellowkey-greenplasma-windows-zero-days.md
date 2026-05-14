---
title: "Researcher Drops YellowKey BitLocker Bypass and GreenPlasma Windows EoP Zero-Days"
date: 2026-05-14 07:27:42 +0000
categories: [Daily Signal]
tags: [zero-day, privilege-escalation, vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/researcher-drops-yellowkey-greenplasma-windows-zero-days/
---

A researcher has publicly released two unpatched Windows zero-days. YellowKey is a BitLocker bypass
that requires physical access to the target machine. GreenPlasma enables elevation of privileges to
System level and does not require physical presence, making it chainable with any remote initial
access vector.

Neither vulnerability has an associated Microsoft patch at time of disclosure. The release coincides
with Pwn2Own Berlin 2026, where exploit research is often accelerated and coordinated disclosures
published. GreenPlasma carries the more immediate risk for networked environments. Monitor Microsoft
Security Response Center for advisories and apply patches or mitigations as they become available.
