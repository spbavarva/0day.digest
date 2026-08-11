---
title: "Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11"
date: 2026-08-11 10:48:26 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/researchers-turn-usb-auto-install-into.html
---

Researchers found that Windows 11 Plug and Play can be abused to fetch
signed vendor software for an emulated USB device, then chain privileged
installation components to gain SYSTEM access on a fully updated machine.
The same Plug and Play path can reportedly be triggered over Remote
Desktop without physical hardware, when supported Plug and Play or
low-level USB redirection is enabled. Microsoft has acknowledged the
technique.
