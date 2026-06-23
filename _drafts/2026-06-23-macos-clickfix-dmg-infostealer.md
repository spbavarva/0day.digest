---
title: "New macOS ClickFix Campaign Uses Mounted DMGs to Push Infostealer"
date: 2026-06-23 18:30:16 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-macos-clickfix-attack-silently-mounts-dmgs-to-push-infostealer/
---

A new ClickFix-style campaign targets macOS users with fake prompts that walk
them through running Terminal commands which silently download, mount, and
launch an info-stealing malware payload from a malicious disk image (DMG)
file. The technique relies on tricking users into manually executing the
malicious commands themselves, sidestepping typical download warnings.
macOS users should be wary of any prompt instructing them to copy and run
Terminal commands from a webpage.
