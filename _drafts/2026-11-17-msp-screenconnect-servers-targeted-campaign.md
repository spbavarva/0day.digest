---
title: "MSP ScreenConnect Servers Targeted in Month-Long Exploitation Campaign"
date: 2026-11-17 13:24:43 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/msp-screenconnect-servers-targeted-in-month-long-campaign/
---

More than 40 ScreenConnect servers used by managed service providers
received over 688,000 malicious requests over a month-long campaign
exploiting CVE-2026-84869 to execute guest-pushed files. The vulnerability
lets attackers run arbitrary files on affected servers via the guest-access
workflow.

MSPs are high-value targets because a single compromised ScreenConnect
instance can provide a path into every downstream client network it
manages. Admins running ScreenConnect should confirm they're patched
against CVE-2026-84869 and audit for unauthorized guest sessions.
