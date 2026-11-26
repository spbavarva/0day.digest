---
title: "Remus Infostealer Steals Gmail Messages via Fake Google Sheets Chrome Extension"
date: 2026-11-26 15:23:28 +0000
categories: [Daily Signal]
tags: [malware, phishing, google]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/remus-malware-steals-gmail-messages-via-fake-google-sheets-extension/
---

The Remus infostealer is being distributed through a malicious Chrome
extension disguised as a Google Sheets add-on. Once installed, the
extension lets the malware read and exfiltrate Gmail messages directly
from the browser session.

Remus operators have reportedly marketed this Gmail-access capability to
other threat actors as a "zero-day exploit" in Google's email service,
though it functions as a browser-extension abuse technique rather than a
flaw in Gmail itself.

Mitigation is restricting installation of unverified Chrome extensions
rather than waiting on a Google-side patch.
