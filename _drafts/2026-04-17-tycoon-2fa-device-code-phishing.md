---
title: "Tycoon 2FA Operators Shift to Device Code Phishing to Bypass MFA"
date: 2026-04-17 19:05:00 +0000
categories: [Daily Signal]
tags: [phishing, iam]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/threat-intelligence/tycoon-2fa-hackers-device-code-phishing
---

The operators behind the Tycoon 2FA adversary-in-the-middle phishing platform have scattered their
infrastructure and are now using device code phishing as a primary account compromise method.

In device code phishing, attackers trick victims into entering a short device code via a service's
legitimate new-device login flow, inadvertently granting the attacker a persistent OAuth access token.
No password theft or inline MFA interception is required — and because the token is issued through the
identity provider's own authentication infrastructure, many conditional access policies do not catch it.

Organizations should restrict or disable OAuth device code authentication flows via Azure AD
Conditional Access or equivalent where not operationally required, monitor for OAuth token grants
from unexpected devices or locations, and update security awareness training to address this specific
phishing pattern.
