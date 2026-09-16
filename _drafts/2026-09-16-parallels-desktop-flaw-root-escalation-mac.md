---
title: "Parallels Desktop Flaw Lets Non-Admin Mac Users Gain Root, but Intel Macs Can't Install Fix"
date: 2026-09-16 13:14:05 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/parallels-desktop-flaw-lets-non-admin.html
---

JFrog disclosed a flaw in Parallels Desktop for Mac that lets a
non-admin local user escalate to root, the highest privilege level on
macOS. Exploitation requires code already running on the machine as a
standard user — it is not exploitable over the network.

Parallels fixed the issue in Parallels Desktop 27, but that version
cannot be installed on Intel-based Macs, leaving those systems without
an available patch.
