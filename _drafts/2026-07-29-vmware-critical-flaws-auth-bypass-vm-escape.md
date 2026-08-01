---
title: "Three Critical VMware Flaws Allow Auth Bypass, Code Execution, VM Escape"
date: 2026-07-29 15:31:15 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html
  - name: SecurityWeek
    url: https://www.securityweek.com/critical-vm-escape-vulnerability-patched-in-vmware-esxi/
---

Broadcom released patches for five vulnerabilities across VMware ESXi,
vCenter, Workstation, and Fusion, three of which are rated critical. The
most severe, CVE-2026-59309 (CVSS 9.8), is an authentication bypass in
vCenter that a network-adjacent attacker can exploit without credentials.
The set also includes a critical remote code execution flaw and a VM
escape vulnerability. No public exploitation has been reported yet.
Administrators running affected VMware products should prioritize
patching, particularly for internet- or network-exposed vCenter instances.
