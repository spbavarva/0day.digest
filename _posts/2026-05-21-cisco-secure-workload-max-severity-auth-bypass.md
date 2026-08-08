---
title: "Cisco Patches Maximum-Severity Auth Bypass in Secure Workload"
date: 2026-05-21 13:58:33 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: critical
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisco-max-severity-secure-workload-flaw-gives-hackers-site-admin-privileges/
---

Cisco patched a maximum-severity vulnerability in Secure Workload (formerly Tetration) where
insufficient validation and authentication in the REST API layer allows remote, unauthenticated
attackers to obtain full Site Admin privileges — granting control over workload segmentation
policy across the environment.

No credentials or prior access are required to trigger the flaw. Cisco released a fixed version;
there is no workaround short of blocking REST API exposure to untrusted networks. Operators
should patch immediately and audit recent Site Admin activity for signs of unauthorized access.
