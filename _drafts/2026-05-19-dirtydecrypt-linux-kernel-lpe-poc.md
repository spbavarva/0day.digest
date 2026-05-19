---
title: "DirtyDecrypt PoC Published for Patched Linux Kernel LPE CVE-2026-31635"
date: 2026-05-19 14:56:26 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation, zero-day]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html
---

Proof-of-concept exploit code has been released for CVE-2026-31635, a Linux kernel local privilege escalation vulnerability dubbed DirtyDecrypt (also known as DirtyCBC).
The vulnerability was discovered by the Zellic and V12 security team on May 9, 2026, and patched in April.
With a public PoC now available, exploitation attempts against unpatched systems are likely to increase rapidly.
Linux system administrators should verify the April kernel patch is applied, particularly on multi-tenant systems, shared hosting environments, and servers where low-privileged or untrusted users can execute code.
Container environments without strict seccomp/AppArmor profiles may also be at risk.
