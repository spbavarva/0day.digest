---
title: "FBI Warns of Kali365 Phishing-as-a-Service Stealing Microsoft 365 OAuth Tokens"
date: 2026-05-22 20:01:00 +0000
categories: [Daily Signal]
tags: [phishing, iam, microsoft, vulnerability]
severity: high
must_know: false
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/fbi-warns-of-kali365-phishing-attacks
---

The FBI issued an advisory on Kali365, a Telegram-based phishing-as-a-service
platform that captures legitimate OAuth tokens rather than passwords. Operators
used it in April 2026 attacks targeting Microsoft 365 environments, bypassing
MFA because the stolen tokens are already authenticated session credentials.

The OAuth token theft approach is increasingly common in PhaaS kits: attackers
proxy the victim through a real M365 login page, harvest the resulting token,
and replay it. Traditional password-based detections miss this entirely.
Defenders should monitor for impossible travel or anomalous token issuance
events in Entra ID sign-in logs, and consider Conditional Access policies that
bind tokens to compliant devices.
