---
title: "VBScript Campaign Spreads Through WhatsApp to Deploy RMM Malware"
date: 2026-06-22 10:00:38 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/whatsapp-vbs-rmm-campaign/120290/
---

Kaspersky researchers identified a global malware campaign that
distributes VBScript files through WhatsApp as the initial infection
vector. The multi-stage infection chain ultimately installs a UEMS
remote monitoring and management (RMM) agent on victim machines, giving
attackers remote control. Using a legitimate RMM tool for persistence
makes the activity harder to distinguish from normal IT operations.
Organizations should monitor for unexpected RMM agent installs and treat
unsolicited script attachments delivered via messaging apps as high-risk.
