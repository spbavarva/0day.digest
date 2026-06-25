---
title: "'Edgecution' Malicious Edge Extension Uses Native Messaging to Escape Browser Sandbox"
date: 2026-06-25 10:11:00 +0000
categories: [Daily Signal]
tags: [malware, ransomware, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/malicious-edge-extension-abuses-native-messaging-as-bridge-to-malware/
---

A malicious Microsoft Edge extension dubbed "Edgecution" was used in a
ransomware attack to escape the browser sandbox by abusing Native Messaging —
the API Chromium-based browsers use to let extensions talk to local native
applications. The technique bridged the sandboxed extension to a Python-based
backdoor on the host, which was then used to deploy ransomware. Native
Messaging is a legitimate, signed channel, so the abuse can slip past
defenses that only inspect extension permissions rather than the native
messaging host processes extensions talk to.
