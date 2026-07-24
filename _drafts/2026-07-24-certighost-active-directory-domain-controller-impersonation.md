---
title: "Certighost Exploit Lets Low-Privileged AD Users Impersonate a Domain Controller"
date: 2026-07-24 14:15:21 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html
---

Researchers H0j3n and Aniq Fakhrul published a working exploit, codenamed
Certighost, that lets a low-privileged Active Directory user obtain a
certificate for a Domain Controller and authenticate as that machine.
Because Domain Controller accounts carry directory replication rights,
the resulting Kerberos credential can be used to retrieve the krbtgt
secret via DCSync — effectively a path to full domain compromise from a
standard user account. AD administrators should review certificate
template permissions and DC impersonation controls.
