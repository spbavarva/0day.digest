---
title: "TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor"
date: 2026-08-30 07:36:33 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html
---

Microsoft disclosed a new ClickFix variant, dubbed TerminalFix, that uses
fake Cloudflare CAPTCHA pages to trick victims into pasting and running a
malicious command.

Unlike traditional ClickFix campaigns that direct victims to the Windows Run
dialog, TerminalFix directs them to Windows Terminal or PowerShell instead,
increasing the odds that more complex, multi-stage commands execute
successfully.

The campaign ultimately deploys a reverse-tunnel backdoor, giving attackers
persistent remote access to compromised systems.
