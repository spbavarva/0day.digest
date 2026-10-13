---
title: "Attackers Chain Three Ivanti Connect Secure Zero-Days for Root Access"
date: 2026-10-13 17:33:11 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, rce, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html
  - name: SecurityWeek
    url: https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/alerts/2026/10/13/cisa-adds-two-known-exploited-vulnerabilities-catalog
---

Security firm Volexity found that an attacker chained three zero-day
vulnerabilities in Ivanti Connect Secure, a VPN appliance, to run commands
as root without authenticating. Ivanti has shipped fixes for two of the
three flaws and told customers on affected versions to act immediately; a
patch for the third is still pending.

CISA has added CVE-2026-104935, an authentication bypass by spoofing in
Connect Secure, to its Known Exploited Vulnerabilities catalog, confirming
active exploitation. Organizations running Ivanti Connect Secure should
apply available patches now and treat unpatched, internet-facing
appliances as potentially compromised.
