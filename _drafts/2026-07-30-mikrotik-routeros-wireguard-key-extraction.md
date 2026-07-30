---
title: "MikroTik RouterOS Flaw Allows WireGuard Private Key Extraction"
date: 2026-07-30 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: medium
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-211-01
---

CISA disclosed CVE-2026-14227, an insufficient session expiration flaw in
MikroTik RouterOS that lets an attacker with only low-privilege API access
extract the router's WireGuard private key in plaintext.

Recovering the key would allow full VPN impersonation and decryption of
associated traffic. The advisory lists all RouterOS versions as affected;
CVSS is scored 4.9, reflecting the low-privilege access prerequisite.
