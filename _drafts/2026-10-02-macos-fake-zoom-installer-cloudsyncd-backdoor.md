---
title: "macOS Users Targeted by Fake Zoom Installer Carrying CloudSyncD Backdoor"
date: 2026-10-02 13:15:00 +0000
categories: [Daily Signal]
tags: [malware, macos]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/macos-users-targeted-by-fake-zoom-installer-carrying-cloudsyncd-backdoor/
---

A fake Zoom installer is dropping a backdoor dubbed CloudSyncD on macOS
systems. The dropper carries a complete universal Mach-O binary embedded
inside itself — roughly 756 KB in the development build analyzed — and
extracts it at runtime.

Users should only download Zoom and similar meeting software from official
sources, and verify installer signatures before running them.
