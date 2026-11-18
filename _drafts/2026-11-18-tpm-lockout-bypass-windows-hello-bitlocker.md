---
title: "New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs"
date: 2026-11-18 12:28:30 +0000
categories: [Daily Signal]
tags: [vulnerability, microsoft, hardware-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html
---

Researchers at Technische Universität Berlin found that the TPM
lockout protecting Windows Hello and BitLocker PINs can be reset on
AMD-based PCs and some Intel PCs by an attacker who opens the device's
case.

Resetting the lockout removes the limit on guess attempts, leaving
short PINs vulnerable to brute-force. In lab tests, researchers
cracked a four-digit Windows Hello PIN on an AMD laptop and a
six-digit BitLocker PIN on an Intel laptop within days rather than the
years the lockout is designed to require.

The attack requires physical access to open the device, but undermines
a core assumption behind TPM-backed PIN protections on affected
hardware.
