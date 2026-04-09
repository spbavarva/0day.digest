---
title: "Atomic Stealer Delivered via ClickFix Script Editor Abuse on macOS"
date: 2026-04-08 18:55:43 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-macos-stealer-campaign-uses-script-editor-in-clickfix-attack/
---

A new macOS campaign delivers Atomic Stealer malware by abusing Script Editor
in a ClickFix variant that tricks users into executing malicious Terminal
commands, bypassing browser-based defenses that typically block drive-by
malware delivery.

The technique exploits user trust in native macOS applications to achieve
execution without browser exploits or signed installers. macOS users should
treat any external instruction to open Script Editor or paste commands into
Terminal as a high-confidence social engineering attempt.
