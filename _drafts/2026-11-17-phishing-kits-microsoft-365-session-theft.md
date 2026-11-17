---
title: "Inside Phishing Kits Built to Steal Microsoft 365 Sessions: EvilTokens, Knight Office, Kali365"
date: 2026-11-17 15:01:11 +0000
categories: [Daily Signal]
tags: [phishing, microsoft]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/inside-modern-phishing-kits-built-to-steal-microsoft-365-sessions/
---

Huntress researchers broke down three modern phishing kits — EvilTokens,
Knight Office, and Kali365 — built specifically to capture and replay
Microsoft 365 session tokens. Token-replay kits let attackers bypass MFA
entirely by hijacking an already-authenticated session rather than
stealing a password.

The report details how each kit operates and offers guidance for
detecting and containing token-theft attacks. Organizations relying on
M365 should ensure session-token binding, conditional access, and
token-theft detection are in place rather than relying on MFA alone.
