---
title: "Fake Android Apps Use WebView Injection and OTP Interception for Carrier Billing Fraud"
date: 2026-05-20 20:35:35 +0000
categories: [Daily Signal]
tags: [malware, phishing, android]
severity: medium
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/mobile-security/fake-android-apps-carrier-billing-fraud
---

Researchers identified a campaign of disguised Android applications that automate carrier billing fraud using WebView automation, JavaScript injection, and OTP interception. The apps silently navigate carrier billing pages, inject scripts to complete subscription flows, and intercept one-time passcodes to bypass confirmation steps. Detection evasion is built in, making them harder to flag via play-store scanning. Users are billed for premium services without consent.
