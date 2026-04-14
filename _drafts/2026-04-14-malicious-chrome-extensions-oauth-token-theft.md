---
title: "100+ Malicious Chrome Extensions in Web Store Steal Google OAuth Tokens and Deploy Backdoors"
date: 2026-04-14 20:33:00 +0000
categories: [Daily Signal]
tags: [malware, data-breach, google, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/over-100-chrome-extensions-in-web-store-target-users-accounts-and-data/
---

More than 100 malicious extensions in the official Chrome Web Store have been discovered
actively stealing Google OAuth2 Bearer tokens, deploying backdoors, and conducting ad fraud.
The extensions abuse broad permissions (cookies, storage, tabs) to silently exfiltrate
authentication tokens, granting attackers persistent access to Google accounts without
requiring a password.

OAuth token theft is particularly dangerous because it bypasses multi-factor authentication
entirely. A stolen Bearer token is a live session credential with no additional challenge.

Users should immediately audit installed Chrome extensions, removing anything recently added
or unfamiliar. Revoke OAuth grants for suspicious third-party applications via Google Account
security settings. Organizations should enforce an allowlist of approved extensions via browser
management policy and review existing extension permissions across their user base.
