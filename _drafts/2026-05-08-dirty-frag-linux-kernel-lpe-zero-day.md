---
title: "Dirty Frag Linux Zero-Day Gives Root on All Major Distributions"
date: 2026-05-08 07:45:24 +0000
categories: [Daily Signal]
tags: [zero-day, privilege-escalation, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/
---

A new unpatched Linux kernel local privilege escalation vulnerability dubbed "Dirty Frag" allows
local attackers to gain root on most major Linux distributions with a single command. A public
proof-of-concept exploit has been released alongside the disclosure. The flaw is described as a
successor to Copy Fail (CVE-2026-31431, CVSS 7.8), a recently disclosed LPE that is already under
active exploitation in the wild. Linux kernel maintainers have been notified but no patch has been
issued as of this writing. Affected distributions are reported to include Debian, Ubuntu, RHEL, and
Fedora. Until a patch is available, organizations should monitor for unexpected privilege escalation
activity and restrict local shell access where possible.
