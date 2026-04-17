---
title: "Windows April 2026 Patches Cause Domain Controller Reboot Loops"
date: 2026-04-17 07:59:00 +0000
categories: [Daily Signal]
tags: [microsoft, vulnerability]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-reboot-loops-affecting-some-domain-controllers/
---

Microsoft has acknowledged that the April 2026 security updates are causing some Windows
domain controllers to enter continuous restart loops after installation. The issue affects
servers running as Active Directory domain controllers.

Organizations that have already applied the April patches and are experiencing DC instability
should consult Microsoft's guidance. Those that have not yet patched should hold off on
deploying to domain controllers until a fix is available or workarounds are confirmed.

The April 2026 Patch Tuesday batch also addressed the Windows zero-days currently under
active exploitation, creating a difficult tradeoff for AD environments between patch urgency
and reboot loop risk.
