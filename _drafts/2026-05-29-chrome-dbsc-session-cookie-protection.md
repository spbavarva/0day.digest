---
title: "Google Rolls Out Device Bound Session Credentials in Chrome to All Users"
date: 2026-05-29 12:08:08 +0000
categories: [Daily Signal]
tags: [google, appsec]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/google-chrome-adds-session-cookie-theft-protection-for-all-users/
---

Google's Device Bound Session Credentials (DBSC) feature is now generally available in Chrome for all users. DBSC cryptographically binds session tokens to the device, preventing stolen cookies from being replayed from another machine.

The feature addresses a common post-phishing escalation path where attackers harvest session cookies via infostealer malware and use them to bypass MFA by replaying the authenticated session elsewhere. With DBSC, a stolen cookie is useless without the corresponding device-held private key.

This is a meaningful defensive control for consumer accounts and organizations using Chrome with Google Workspace. Adoption by other sites and identity providers via the DBSC standard will determine how broadly it reduces account takeover in the wild.
