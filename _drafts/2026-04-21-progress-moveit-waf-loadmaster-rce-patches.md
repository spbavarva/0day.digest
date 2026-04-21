---
title: "Progress Patches RCE, OS Command Injection, and WAF Bypass in MOVEit and LoadMaster"
date: 2026-04-21 12:14:26 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/progress-patches-multiple-vulnerabilities-in-moveit-waf-loadmaster/
---

Progress Software has released patches for multiple vulnerabilities in MOVEit Transfer WAF and
LoadMaster, including flaws that enable remote code execution, OS command injection, and WAF
detection bypass. MOVEit Transfer is the managed file transfer platform that was the target of
the mass supply chain exploitation campaign in 2023, making any new critical patches
high-priority regardless of active exploitation status.

The WAF bypass vulnerability is especially concerning: it could allow attackers to exploit
additional vulnerabilities while evading perimeter detection, compounding the risk of the other
flaws. OS command injection and RCE in these components provide a path to full system compromise
of MOVEit infrastructure.

Organizations running MOVEit Transfer WAF or LoadMaster should apply Progress's patches
immediately. Given MOVEit's history as an active mass-exploitation target, assume that patches
will be reverse-engineered quickly and exploitation attempts will follow shortly after disclosure.
