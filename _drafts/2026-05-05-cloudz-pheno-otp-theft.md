---
title: "CloudZ RAT 'Pheno' Plugin Hijacks Microsoft Phone Link to Steal SMS and OTPs"
date: 2026-05-05 10:00:00 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/cloudz-pheno-infostealer/
---

Cisco Talos has discovered a new version of the CloudZ remote access tool (RAT) deploying a previously undocumented plugin called "Pheno." The plugin hijacks the Microsoft Phone Link application's established Bluetooth/Wi-Fi pairing connection between a Windows host and paired Android device to intercept SMS messages and OTP codes in real time. This bypasses SMS-based MFA without requiring the attacker to compromise the mobile device directly. The intrusion has been active since at least January 2026. Organizations relying on SMS OTPs for authentication should treat this as a prompt to migrate to phishing-resistant MFA. Windows environments with Phone Link enabled and any active RAT infection are at elevated risk of MFA bypass.
