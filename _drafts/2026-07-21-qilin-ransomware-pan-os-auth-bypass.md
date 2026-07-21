---
title: "Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access"
date: 2026-07-21 14:04:57 +0000
categories: [Daily Signal]
tags: [ransomware, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
---

Arctic Wolf Labs investigated multiple intrusions in June 2026 that began
with exploitation of CVE-2026-0257 (CVSS 7.8), a high-severity
authentication bypass affecting the Palo Alto Networks PAN-OS
GlobalProtect portal and gateway. Threat actors used the now-patched flaw
as an entry point to deploy Qilin (aka Agenda) ransomware on victim
environments. Organizations running PAN-OS should confirm they're patched
against CVE-2026-0257.
