---
title: "PoC Released for DirtyDecrypt Linux Kernel Privilege Escalation to Root"
date: 2026-05-19 09:42:56 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/poc-released-for-dirtydecrypt-linux-kernel-vulnerability/
---

A proof-of-concept exploit has been publicly released for DirtyDecrypt, a
Linux kernel vulnerability patched in April 2026 that allows local attackers
to escalate privileges to root. The PoC release significantly lowers the bar
for exploitation by any attacker with local access to an unpatched system.

Linux hosts that haven't applied April 2026 kernel updates are now at
heightened risk, especially multi-tenant environments, container hosts, or
systems where users can run arbitrary code. Patch immediately; until patched,
treat any local code execution on affected hosts as equivalent to root
compromise.
