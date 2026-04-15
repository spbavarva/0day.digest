---
title: "Microsoft Adds Windows Warnings for Malicious .RDP Files to Counter Phishing Attacks"
date: 2026-04-14 22:23:33 +0000
categories: [Daily Signal]
tags: [microsoft, phishing, vulnerability]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-adds-windows-protections-for-malicious-remote-desktop-files/
---

Microsoft has introduced new Windows protections targeting phishing campaigns that abuse Remote
Desktop Protocol (.rdp) files. The changes include user-facing warnings when opening .rdp files
from untrusted sources, and default disabling of risky shared resources (clipboard forwarding,
local drive redirection) in Remote Desktop connections.

Phishing campaigns delivering malicious .rdp file attachments have been an active initial access
tactic, enabling attackers to establish Remote Desktop sessions to attacker-controlled servers
and harvest credentials or deploy implants in the process.

The new protections are a meaningful but incomplete defense — users can still dismiss warnings.
Security teams should enforce Group Policy to restrict .rdp file execution where Remote Desktop
is not operationally required, and configure email gateways to block or quarantine .rdp
attachments.
