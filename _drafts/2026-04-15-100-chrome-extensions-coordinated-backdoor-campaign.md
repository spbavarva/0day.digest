---
title: "100 Chrome Extensions in Coordinated Campaign Steal User Data and Open Backdoors"
date: 2026-04-15 13:24:00 +0000
categories: [Daily Signal]
tags: [malware, data-breach, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/100-chrome-extensions-steal-user-data-open-backdoor/
---

Researchers have identified 100 malicious Chrome browser extensions published through five
separate developer accounts that steal user data and create backdoor access. The extensions
share common command-and-control infrastructure, confirming a coordinated campaign rather than
isolated bad actors.

The use of multiple developer accounts to distribute a large extension fleet is a known technique
for surviving Google's moderation process—when one account is banned, others continue
distributing the same payload under different names. Shared C2 infrastructure indicates
centralized control over the full fleet.

Users should audit installed Chrome extensions, removing any from unfamiliar publishers.
Enterprise security teams should enforce extension allowlists via policy and monitor for
extensions requesting broad permissions such as access to all websites, clipboard, or browser
history.
