---
title: "Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections"
date: 2026-10-21 10:30:27 +0000
categories: [Daily Signal]
tags: [malware, credential-theft, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
---

A researcher found that more than 300 Tor exit relays were taken over by
attackers in early October and used to intercept traffic leaving the Tor
network. Between October 1 and 5, password-based SSH logins routed
through the compromised exit relays were redirected to servers that
harvested the login credentials.

Exit relays sit at the last hop of a Tor circuit, giving an attacker
visibility into unencrypted traffic as it leaves the network. Anyone who
completed a password-authenticated SSH login over Tor during that window
should rotate the affected credentials.
