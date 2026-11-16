---
title: "A USB Worm's Second Life: Retadup Delivers CoffeeLoader"
date: 2026-11-16 07:00:37 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/retadup-delivers-coffeeloader/121908/
---

Kaspersky disclosed a new variant of CoffeeLoader malware spreading through
Retadup, a USB worm whose original infrastructure was seized by law
enforcement in 2019.

The NSIS-based installer drops a file named "7z.dll" into a temporary
directory and runs it via rundll32.exe; that file is a patched, malicious
version of a legitimate library component used to load the next stage. The
resurgence shows old worm infrastructure and techniques still being
repurposed for current malware delivery.
