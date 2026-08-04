---
title: "Malware Can Hijack Passkey-Protected Google Accounts Without User Interaction"
date: 2026-08-03 16:24:47 +0000
categories: [Daily Signal]
tags: [vulnerability, google, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/google-password-manager-attacks-could.html
---

Unit 42 researchers detailed three attack paths against Chrome's Google
Password Manager cloud authenticator — Pass-ta-key, Silver Pass-ta-key, and
Golden Pass-ta-key. Malware running with only ordinary user privileges on a
Windows machine can sign into a victim's passkey-protected accounts without a
fingerprint, PIN, or any visible prompt. The strongest variant, Golden
Pass-ta-key, targets the master key protecting all passkeys stored in the
password manager. This undermines a core assumption of passkey
authentication: that a stolen credential alone isn't enough without a
device-bound second factor.
