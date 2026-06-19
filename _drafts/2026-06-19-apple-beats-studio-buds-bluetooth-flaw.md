---
title: "Apple Patches Beats Studio Buds Bluetooth Flaw Enabling Nearby Eavesdropping"
date: 2026-06-19 06:36:09 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html
---

Apple patched a high-severity vulnerability, CVE-2025-20701 (CVSS 8.8),
affecting the Airoha Bluetooth audio SDK used in Beats Studio Buds. The flaw
is an incorrect-authorization bug that allows pairing with the earbuds
without user consent. A nearby attacker could exploit this to eavesdrop via
the device's microphone. The Airoha SDK is used across multiple Bluetooth
audio products, so other vendors' hardware using the same chipset may carry
similar exposure. Users should update Beats Studio Buds firmware as soon as
it's available through the Apple ecosystem.
