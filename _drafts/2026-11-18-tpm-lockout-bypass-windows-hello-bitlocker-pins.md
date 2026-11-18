---
title: "New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs"
date: 2026-11-18 12:28:30 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html
---

Researchers at Technische Universität Berlin found that on AMD-based PCs and
some Intel PCs, the TPM lockout protecting Windows Hello and BitLocker PINs
can be reset by someone who opens the device's case, removing the
brute-force protection.

In lab tests this let them crack a four-digit Windows Hello PIN and a
six-digit BitLocker PIN within days instead of the years the lockout is
designed to require. The attack requires physical access to the device.
