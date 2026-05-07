---
title: "Microsoft Details AitM Phishing Campaign That Stole Tokens from 35,000 Users Across 26 Countries"
date: 2026-05-05 06:35:00 +0000
categories: [Daily Signal]
tags: [phishing, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html
---

Microsoft has published a detailed breakdown of a large-scale adversary-in-the-middle (AitM) credential theft campaign observed April 14–16, 2026. The operation targeted over 35,000 users across more than 13,000 organizations in 26 countries. Attackers used conduct report-themed email lures sent via legitimate email service providers to evade spam filters, then redirected victims to attacker-controlled domains that proxied real Microsoft login pages to steal session tokens — bypassing MFA in the process. The AitM infrastructure allowed real-time token capture without requiring victim credentials in plaintext. Security teams should review Conditional Access policies for risky sign-in detections in the April 14–16 window and consider enforcing phishing-resistant authentication (FIDO2/passkeys) for high-value accounts.
