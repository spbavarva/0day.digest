---
title: "VoidStealer Trojan Bypasses Chrome App-Bound Encryption to Steal Credentials"
date: 2026-05-06 21:19:11 +0000
categories: [Daily Signal]
tags: [vulnerability, malware, google, appsec]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/endpoint-security/yet-another-way-bypass-google-chromes-encryption-protection
---

Authors of the VoidStealer information-stealing Trojan discovered a new technique to bypass Google Chrome's App-Bound Encryption (ABE), a protection introduced to prevent credential theft from the browser. The bypass enables infostealer malware to extract stored passwords and session tokens from Chrome. This is at least the second publicly known ABE bypass method, indicating the protection is under active pressure from infostealer authors. Endpoint security teams should ensure infostealer detections are current and treat Chrome-stored credentials as potentially at risk in high-threat environments.
