---
title: "Sandworm Uses Fake CAPTCHA to Trick Ukrainians Into Running PowerShell"
date: 2026-07-16 13:50:00 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/ukraine-sandworm-hacks-captcha-powershell
---

Russian state-linked group Sandworm is targeting Ukrainian users with fake
CAPTCHA verification pages that, instead of confirming the user is human,
instruct them to copy and paste a PowerShell command into their Windows
machine. This ClickFix-style social engineering technique bypasses
technical exploitation entirely, relying on user-executed commands for
initial access. Defenders should treat CAPTCHA pages requesting terminal or
PowerShell interaction as a red flag.
