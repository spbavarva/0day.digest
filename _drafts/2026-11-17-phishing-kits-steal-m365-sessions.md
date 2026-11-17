---
title: "Researchers Detail Phishing Kits Built to Steal Microsoft 365 Sessions"
date: 2026-11-17 15:01:11 +0000
categories: [Daily Signal]
tags: [phishing, appsec]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/inside-modern-phishing-kits-built-to-steal-microsoft-365-sessions/
---

Huntress researchers published a breakdown of three active phishing kits —
EvilTokens, Knight Office, and Kali365 — built specifically to capture and
replay Microsoft 365 session tokens. By stealing valid session tokens
rather than just credentials, these kits let attackers bypass MFA and
access accounts without triggering a fresh login challenge.

The research also covers detection and containment guidance for defenders.
Organizations relying on M365 should review session-token monitoring and
conditional access policies in light of these techniques.
