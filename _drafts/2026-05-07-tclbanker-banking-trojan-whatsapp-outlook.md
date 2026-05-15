---
title: "TCLBanker Trojan Targets 59 Financial Platforms, Spreads via WhatsApp and Outlook"
date: 2026-05-07 22:06:52 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-tclbanker-malware-self-spreads-over-whatsapp-and-outlook/
---

A new banking trojan named TCLBanker is being distributed via a trojanized MSI installer masquerading
as Logitech AI Prompt Builder. The malware targets 59 banking, fintech, and cryptocurrency platforms
and self-propagates by sending malicious links through the victim's WhatsApp and Outlook accounts.
The use of a legitimate-looking Logitech software installer is a classic supply-chain lure, and the
self-spreading behavior via trusted communication channels significantly amplifies reach. Users and
organizations should block unsigned MSI installers from untrusted sources and monitor for anomalous
messaging behavior from endpoint accounts.
