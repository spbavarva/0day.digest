---
title: "15-Year-Old OpenSSH Flaw Allowed Full Root Shell Access via Certificate Principal Parsing Bug"
date: 2026-04-27 12:29:18 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, privilege-escalation, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/openssh-flaw-allowing-full-root-shell-access-lurked-for-15-years/
---

A vulnerability present in OpenSSH for approximately 15 years has been discovered and patched. A code reuse issue caused comma characters in certificate principals to be interpreted as list separators, enabling an attacker with a crafted SSH certificate to obtain a full root shell.

The flaw affects OpenSSH installations using certificate-based authentication. Systems relying on SSH certificates for access — common in large-scale or cloud environments — should update immediately. The 15-year window means long-running production systems that have never performed a full OpenSSH upgrade may be affected. Review SSH certificate authority configurations for any abnormal principal assignments.
