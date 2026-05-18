---
title: "DirtyDecrypt: Public PoC Released for Linux Kernel Root Escalation Flaw"
date: 2026-05-18 07:18:33 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability, cve, linux, container-security]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/
---

A public proof-of-concept exploit is now available for DirtyDecrypt, a recently patched local
privilege escalation vulnerability in the Linux kernel's `rxgk` module. The flaw allows an attacker
with local access to gain root on affected Linux systems.

Container environments and multi-tenant Linux hosts are particularly at risk since local access is
commonly available to unprivileged workloads. Confirm your kernel version against vendor security
advisories and patch promptly; the existence of a public PoC means exploitation should be considered
likely on unpatched systems.
