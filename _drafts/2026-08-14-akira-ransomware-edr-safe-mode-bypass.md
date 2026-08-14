---
title: "Akira Hackers Disable EDR With Safe Mode, Steal Data but Fail to Encrypt"
date: 2026-08-14 20:47:02 +0000
categories: [Daily Signal]
tags: [ransomware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/
---

An Akira ransomware affiliate disabled endpoint detection and response (EDR)
tooling on a compromised system by rebooting it into Safe Mode with
Networking, since many EDR agents don't load in that state. The affiliate
exfiltrated data but ultimately failed to complete encryption.

Defenders should ensure EDR/security agents are configured to start in Safe
Mode, and treat unexpected Safe Mode reboots as a detection trigger.
