---
title: "Device Code Phishing Attack Abuses a Microsoft Sign-In Page"
date: 2026-07-06 09:00:43 +0000
categories: [Daily Signal]
tags: [phishing, microsoft]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/microsoft-device-code-phishing-attack/120350/
---

The OAuth 2.0 Device Authorization Grant flow, built to simplify sign-in for
Smart TVs, IoT devices, and printers, is being weaponized in a phishing
campaign that spoofs a Microsoft sign-in page. Victims are tricked into
approving a device code that hands the attacker a valid session token,
sidestepping the usual "check the URL" advice since the phishing page can
look entirely legitimate. Kaspersky's GReAT team documented the technique as
part of ongoing threat intel on device-code phishing. Organizations that
support device code login should monitor for anomalous approvals and
restrict the flow where it isn't needed.
