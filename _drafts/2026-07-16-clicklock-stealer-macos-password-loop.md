---
title: "ClickLock Stealer Kills macOS Apps Every 210ms Until Victims Type Their Password"
date: 2026-07-16 12:33:42 +0000
categories: [Daily Signal]
tags: [malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html
---

A new macOS infostealer called ClickLock Stealer coerces victims into
entering their password by repeatedly killing running applications until
they comply. It's delivered as a command pasted into Terminal, then shows a
fake system dialog requesting the password; if the victim cancels, it
installs two LaunchAgents and exits quietly, resuming the kill loop at the
next login across Finder, Dock, Spotlight, Terminal, and Activity Monitor.
The malware has targeted at least 100 users to steal passwords and
cryptocurrency, relying on social engineering rather than a software
exploit.
