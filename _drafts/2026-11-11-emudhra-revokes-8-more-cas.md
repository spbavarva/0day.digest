---
title: "eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise"
date: 2026-11-11 12:00:53 +0000
categories: [Daily Signal]
tags: [pki]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/emudhra-revokes-8-more-ca-certificates-after-private-key-mishap/
---

eMudhra revoked eight more intermediate CA certificates that it had
previously declared unaffected by its October key-compromise incident.
The newly revoked CAs had a different problem from the originally
compromised ones: a single line in the in-house Python script eMudhra
uses to generate certificates caused an issue, even though it didn't
weaken the keys themselves. BleepingComputer separately confirmed the
investigation found improper handling of private keys during the
certificate-generation process.

Organizations relying on certificates from the affected intermediate
CAs should check for reissuance guidance from eMudhra.
