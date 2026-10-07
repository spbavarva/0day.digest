---
title: "Attackers Hijack .gh, .sl, and .as Registries to Obtain Certificates for Google Domains"
date: 2026-10-07 18:48:17 +0000
categories: [Daily Signal]
tags: [vulnerability, google, supply-chain]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html
---

Attackers compromised three country-code top-level domain registries —
Ghana's .gh, Sierra Leone's .sl, and American Samoa's .as — and used that
access to obtain unauthorized HTTPS certificates for several Google domains,
Google disclosed on October 6.

Google's own systems were not breached. The attackers compromised
third-party registry operators and modified authoritative DNS records,
putting any domain ending in .gh, .sl, or .as at risk of impersonation. A
certificate obtained this way could let an attacker pose as the real site
over an encrypted connection.
</content>
