---
title: "Storm-2755 Hijacks Accounts to Redirect Canadian Employee Payroll"
date: 2026-04-10 11:56:14 +0000
categories: [Daily Signal]
tags: [phishing, microsoft]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-canadian-employees-targeted-in-payroll-pirate-attacks/
---

Microsoft has identified Storm-2755, a financially motivated threat actor conducting
"payroll pirate" attacks that compromise employee accounts and then modify direct
deposit banking information within payroll systems before victims notice. The campaign
is currently targeting Canadian employees. Once inside an account, attackers reroute
salary payments to attacker-controlled accounts, often going undetected until a missed
payday. Organizations should enforce MFA on payroll and HR platforms, restrict access
to banking information changes, and implement approval workflows or delays for direct
deposit modifications. Monitoring for account access from new geolocations or devices
immediately followed by payroll changes is an effective detection pattern.
