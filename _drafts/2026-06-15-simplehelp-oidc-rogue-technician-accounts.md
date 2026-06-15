---
title: "SimpleHelp Flaw Lets Unauthenticated Attackers Create Rogue Technician Accounts"
date: 2026-06-15 20:06:52 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/simplehelp-bug-lets-hackers-create-rogue-remote-support-accounts/
---

A vulnerability in SimpleHelp's remote support software allows unauthenticated attackers to create privileged technician accounts on managed servers.
The flaw lies in how SimpleHelp handles OpenID Connect (OIDC) authentication, letting an attacker register a new account with technician-level access without valid credentials.
A rogue technician account grants the same remote-access capabilities as a legitimate support account on any endpoint managed through that SimpleHelp instance.
Administrators should review their SimpleHelp technician account lists for unrecognized entries and apply the vendor's update once available.
