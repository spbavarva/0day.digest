---
title: "Dirty Frag: Unpatched Linux Zero-Day Gives Root on All Major Distros"
date: 2026-05-08 07:45:24 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, privilege-escalation, cve, linux]
severity: critical
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/
---

A new unpatched local privilege escalation vulnerability dubbed "Dirty Frag" affects all major Linux
distributions, with a public PoC that grants root access in a single command. It is the successor to
Copy Fail (CVE-2026-31431), an LPE flaw already under active exploitation. Dirty Frag has been
disclosed to Linux kernel maintainers, but no patch is available yet. Linux server operators and
container hosts should restrict local shell access and monitor kernel update channels closely.
