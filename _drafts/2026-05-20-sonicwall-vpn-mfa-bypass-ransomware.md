---
title: "Attackers Bypass SonicWall VPN MFA via Incomplete Patch, Deploy Ransomware"
date: 2026-05-20 21:19:17 +0000
categories: [Daily Signal]
tags: [ransomware, vulnerability, vpn]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-bypass-sonicwall-vpn-mfa-due-to-incomplete-patching/
---

Threat actors brute-forced credentials on SonicWall Gen6 SSL-VPN appliances and then bypassed multi-factor authentication due to an incompletely applied patch. Successful exploitation gave attackers persistent VPN access, which they leveraged to deploy ransomware tooling. Organizations using Gen6 SSL-VPN should verify that the latest patch revision is fully applied — partial patching appears to leave the MFA bypass vector open.
