---
title: "Microsoft Working on Patch for 'RoguePlanet' Zero-Day"
date: 2026-06-17 09:41:07 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, privilege-escalation, microsoft]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/microsoft-working-on-patch-for-rogueplanet-zero-day/
---

Public proof-of-concept code exploits a race condition in Microsoft Defender
that lets a local attacker spawn a command prompt with SYSTEM privileges.
Microsoft has acknowledged the flaw, dubbed "RoguePlanet," and is working on
a patch, but none has shipped yet. Because Defender ships by default on most
Windows systems, the unpatched window affects a broad install base.
Defenders should watch for unexpected SYSTEM-level process spawns tied to
Defender activity until a fix is available.
