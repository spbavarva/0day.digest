---
title: "Qilin and INC Ransomware Groups Exploit Palo Alto Networks Flaw to Bypass MFA"
date: 2026-10-20 15:32:27 +0000
categories: [Daily Signal]
tags: [ransomware, cve, vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/qilin-and-inc-ransomware-groups-exploit.html
---

Palo Alto Networks confirmed continued exploitation of CVE-2026-0257, an
authentication bypass flaw (CVSS 7.8) in PAN-OS and Prisma Access, by the
Qilin and INC ransomware groups. The flaw lets attackers set up unauthorized
VPN connections, bypassing MFA.

It was patched in May 2026, but exploitation is ongoing against
organizations that haven't updated. Practitioners running PAN-OS or Prisma
Access should confirm patch status and audit for unauthorized VPN sessions.
