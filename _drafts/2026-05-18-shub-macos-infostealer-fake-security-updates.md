---
title: "SHub macOS Infostealer Variant Spoofs Apple Security Updates to Install Backdoor"
date: 2026-05-18 21:42:20 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/shub-macos-infostealer-variant-spoofs-apple-security-updates/
---

A new SHub macOS infostealer variant uses AppleScript to display a convincing
fake Apple security update prompt, tricking users into authorizing installation
of a persistent backdoor. The social engineering lure exploits the trust users
place in Apple system-level alerts.

macOS users should verify that software updates only arrive through System
Settings → Software Update and be suspicious of any browser-based or app-based
prompts claiming to install security patches. Security teams should look for
unusual AppleScript execution or unexpected LaunchAgent/LaunchDaemon entries
as potential indicators.
