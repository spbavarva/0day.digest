---
title: "Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps"
date: 2026-08-18 17:47:22 +0000
categories: [Daily Signal]
tags: [llm, microsoft, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html
---

Varonis Threat Labs disclosed three vulnerabilities in Microsoft Copilot
Personal, collectively named "CoSnitch," that could allow a single click on
a crafted link to silently pull data from apps connected to a victim's
Copilot session.

The flaws turn in part on an undocumented URL parameter that the assistant
itself surfaces, which attackers can leverage to trigger the exfiltration
without further victim interaction.
