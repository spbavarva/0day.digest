---
title: "Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs"
date: 2026-07-23 08:04:35 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/nine-year-old-refluxfs-linux-flaw-gives.html
---

A nine-year-old race condition in the Linux kernel's XFS filesystem, tracked
as CVE-2026-64600 and dubbed RefluXFS, lets an unprivileged local attacker
overwrite root-owned files and gain persistent root access. Qualys says
default installations of Red Hat Enterprise Linux and its derivatives,
Fedora Server, and Amazon Linux can meet the conditions for exploitation,
and the firm demonstrated a working race-condition exploit. The flaw
requires local access; no remote exploitation vector was described.
Administrators should watch for a kernel patch and prioritize systems with
local multi-user access.
