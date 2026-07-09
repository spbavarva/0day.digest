---
title: "'GodDamn' Ransomware Uses Signed Malicious Driver to Kill Security Software"
date: 2026-07-09 10:00:00 +0000
categories: [Daily Signal]
tags: [ransomware, malware, privilege-escalation]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/goddamn-ransomware-byovd-smite-companies
---

Ransomware operators are using a bring-your-own-vulnerable-driver (BYOVD)
technique against US companies, deploying a kernel driver that Microsoft
itself co-signed. The signed driver is abused to terminate security
software and EDR agents before the ransomware payload runs, letting
attackers operate with reduced detection risk. Organizations should ensure
driver-blocklist protections (e.g. Microsoft's vulnerable driver blocklist)
are current and monitor for unexpected kernel driver loads.
