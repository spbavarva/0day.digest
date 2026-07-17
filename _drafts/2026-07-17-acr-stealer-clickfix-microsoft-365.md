---
title: "ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files"
date: 2026-07-17 08:56:39 +0000
categories: [Daily Signal]
tags: [malware, phishing, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
---

ACR Stealer, an infostealer in circulation since 2024, is using ClickFix-style lures that trick victims into pasting and running a command via the Windows Run box. Once executed, it pulls saved browser passwords, live session tokens, PDFs, Microsoft 365 documents, and files from synced OneDrive and SharePoint folders. Microsoft's Defender Experts team detailed two separate delivery chains behind the current wave. Organizations should reinforce user awareness around "paste this to fix an issue" prompts, a hallmark of the ClickFix technique.
