---
title: "New Pass-ta-key Attacks Let Malware Hijack Google-Synced Passkeys"
date: 2026-08-03 23:58:01 +0000
categories: [Daily Signal]
tags: [malware, google, vulnerability]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-pass-ta-key-attacks-let-malware-hijack-google-synced-passkeys/
---

Researchers disclosed three attack techniques, dubbed "Pass-ta-key," that
let malware already running on a compromised Windows device abuse Google
Password Manager's synced passkeys. The attacks bypass user verification and
can extract passkey private keys, letting attackers take over accounts
protected by passkeys.

The findings undercut the assumption that passkey private keys can't be
exfiltrated once synced. Passkeys still stop remote phishing, but the
research shows they don't fully protect against an already-compromised
device.
