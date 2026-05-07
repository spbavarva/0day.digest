---
title: "CloudZ RAT Abuses Windows Phone Link to Steal Credentials and Bypass 2FA"
date: 2026-05-06 08:34:00 +0000
categories: [Daily Signal]
tags: [malware, phishing, microsoft, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/windows-phone-link-exploited-by-cloudz.html
---

Researchers disclosed the CloudZ remote access trojan paired with a previously undocumented plugin called Pheno that abuses Windows Phone Link to bridge a victim's PC and smartphone. The combination enables interception of credentials and one-time passwords, effectively bypassing SMS-based two-factor authentication.

The technique operates through a legitimate Windows feature rather than injecting into browsers or intercepting network traffic, making it harder to detect. Security teams should consider disabling Windows Phone Link on sensitive or high-risk endpoints, and organizations relying on SMS OTP for MFA should accelerate migration to phishing-resistant authenticators (FIDO2 or app-based TOTP).
