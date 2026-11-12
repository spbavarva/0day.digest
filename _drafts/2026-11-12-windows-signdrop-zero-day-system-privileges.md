---
title: "New Windows SignDrop Zero-Day Gives Hackers SYSTEM Privileges"
date: 2026-11-12 16:04:00 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/
---

Security researcher Abdelhamid Naceri (aka Nightmare Eclipse) released a
new Windows zero-day exploit, dubbed SignDrop, that can let a local
attacker gain SYSTEM privileges. The exploit targets a log-authentication
feature added to the Common Log File System (CLFS) driver last year.

SignDrop abuses how clfs.sys creates companion files when a privileged
process opens a prepared log, using path redirection to seize control. No
patch was available at the time of disclosure.
