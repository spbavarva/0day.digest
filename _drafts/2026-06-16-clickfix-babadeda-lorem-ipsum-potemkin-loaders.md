---
title: "ClickFix Campaigns Deploy Three New Malware Loaders Targeting Education and Finance"
date: 2026-06-16 17:41:00 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html
---

Researchers from Morphisec, BlueVoyant, and Huntress have independently documented three new ClickFix campaigns delivering malware loaders BabaDeda, Lorem Ipsum, and Potemkin. BabaDeda attacks observed in April 2026 targeted education and financial organizations; Lorem Ipsum leverages compromised WordPress sites and is tentatively linked to the ransomware and data-extortion group Vice Society; Potemkin relies on fake browser update lures. ClickFix is a social engineering technique that tricks users into executing malicious clipboard commands via browser pop-ups disguised as error dialogs. Defenders should enforce browser clipboard-write restrictions in hardened policies and monitor for unusual PowerShell or wscript execution chains following browser interaction.
