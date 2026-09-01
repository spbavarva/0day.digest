---
title: "WatchGuard Patches Critical Fireware OS Vulnerabilities"
date: 2026-09-01 08:50:04 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/watchguard-patches-critical-vulnerabilities/
---

WatchGuard has patched three critical vulnerabilities in the Fireware
OS iked process, which handles IKE/IPsec VPN negotiation. The flaws
could allow an unauthenticated attacker to execute arbitrary code
remotely.

No evidence of active exploitation was reported at the time of
disclosure. Because iked is typically network-reachable in VPN
gateway deployments, administrators running affected Fireware OS
versions should apply the patches promptly.
