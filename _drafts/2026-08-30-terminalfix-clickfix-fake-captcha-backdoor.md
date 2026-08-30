---
title: "TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor"
date: 2026-08-30 07:36:33 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html
---

Microsoft disclosed a new ClickFix variant called TerminalFix. Where
traditional ClickFix campaigns lure victims into pasting commands into
the Windows Run dialog, TerminalFix uses fake Cloudflare CAPTCHA pages
to direct victims to Windows Terminal or PowerShell instead.

Running the malicious command in a full terminal rather than the Run
dialog increases the odds that more complex commands execute
successfully. The technique is used to deploy a reverse-tunnel
backdoor on infected machines.
