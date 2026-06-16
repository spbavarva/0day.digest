---
title: "SearchLeak: One-Click Flaw Chain in Microsoft 365 Copilot Enabled Mail and File Exfiltration"
date: 2026-06-15 15:09:05 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, microsoft, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-attack-turned-microsoft-365-copilot-into-1-click-data-theft-tool/
---

Researchers at Varonis Threat Labs chained three vulnerabilities in Microsoft 365 Copilot Enterprise Search into an attack they call SearchLeak.
A single click on a link could let an attacker exfiltrate emails, calendar details, indexed files, and even MFA codes from a victim's Microsoft 365 account.
Because the malicious link pointed to a legitimate microsoft.com domain, traditional anti-phishing and URL-filtering tools did not flag it.
The chain could expose data from a target's mailbox, OneDrive, and SharePoint through a specially crafted URL.
Organizations using Microsoft 365 Copilot Enterprise Search should confirm they're on a patched configuration and review Copilot access logs for unusual search activity.
