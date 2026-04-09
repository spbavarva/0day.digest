---
title: "Google Chrome 146 Ships Device Bound Session Credentials to Block Infostealer Cookie Theft"
date: 2026-04-09 18:33:00 +0000
categories: [Daily Signal]
tags: [appsec, google, malware]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/google-chrome-adds-infostealer-protection-against-session-cookie-theft/
---

Google has enabled Device Bound Session Credentials (DBSC) in Chrome 146 for Windows as a
default protection against session cookie theft by infostealer malware. DBSC cryptographically
ties session tokens to the device's hardware, rendering cookies stolen by malware useless on
attacker-controlled machines.

Infostealers including Redline, Vidar, and Lumma have made browser session cookie harvesting
one of the most common initial access techniques — enabling full account takeover without
requiring a password or MFA bypass. DBSC is a meaningful architectural defense that cuts off
this specific attack path. No user action is required; Chrome 146 enables DBSC automatically
on supported Windows configurations. Enterprise teams should verify compatibility with SSO,
SAML, and browser-based authentication providers and test rollout in staging environments
before broad deployment.
