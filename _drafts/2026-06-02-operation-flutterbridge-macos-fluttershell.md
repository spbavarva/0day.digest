---
title: "Operation FlutterBridge: macOS Malvertising Campaign Distributes New FlutterShell Backdoor"
date: 2026-06-02 10:00:00 +0000
categories: [Daily Signal]
tags: [malware, appsec, phishing]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/
---

Unit 42 has detailed Operation FlutterBridge, a macOS malvertising campaign distributing a new backdoor called FlutterShell. The malware is built using Flutter — the cross-platform UI framework — as a technique to complicate static analysis and evade detection tools that are tuned for traditional macOS binary formats. The campaign delivers malicious installers through malvertising to macOS users who click on poisoned ads. FlutterShell establishes persistence and provides remote access to compromised systems. macOS defenders should review ad-blocking and browser protection controls, and apply detection rules for Flutter-packaged executables exhibiting post-exploitation behavior.
