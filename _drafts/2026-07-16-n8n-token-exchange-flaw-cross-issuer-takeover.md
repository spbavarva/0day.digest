---
title: "n8n Enterprise Token Exchange Flaw Enables Cross-Issuer Account Takeover"
date: 2026-07-16 13:33:25 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
---

A flaw in n8n's Enterprise token exchange logic let attackers log in as
other users on instances configured to trust more than one external token
issuer. The bug matched an incoming JWT to a local account using only the
sub claim, ignoring the iss (issuer) claim — so a valid token from Issuer A
carrying a sub matching a user under Issuer B would authenticate as that
user, without needing their password. Organizations running n8n Enterprise
with multiple trusted token issuers should confirm they're on a patched
version.
