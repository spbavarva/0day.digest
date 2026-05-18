---
title: "MiniPlasma Windows Zero-Day Grants SYSTEM Privileges on Fully Patched Systems"
date: 2026-05-18 08:57:34 +0000
categories: [Daily Signal]
tags: [zero-day, privilege-escalation, vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html
---

Researcher "Chaotic Eclipse" has released a public proof-of-concept exploit for MiniPlasma, a
Windows privilege escalation zero-day that grants SYSTEM privileges on fully patched systems. The
vulnerability targets `cldflt.sys` (Windows Cloud Files Mini Filter Driver) and is the third Windows
flaw disclosed by this researcher after YellowKey and GreenPlasma.

No Microsoft patch is currently available. The public PoC substantially lowers the exploitation bar.
Defenders should monitor for suspicious activity involving cldflt.sys, flag anomalous privilege
escalation attempts, and apply any forthcoming Microsoft patch as a priority.
