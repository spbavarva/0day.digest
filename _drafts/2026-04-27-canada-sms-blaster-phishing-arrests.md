---
title: "Canada Arrests Three for Running SMS Blaster That Injected Phishing Texts at Radio Layer"
date: 2026-04-27 20:00:31 +0000
categories: [Daily Signal]
tags: [phishing]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/canada-arrests-three-for-operating-sms-blaster-device-in-toronto/
---

Canadian police arrested three individuals in Toronto for operating a commercial IMSI catcher (SMS blaster) that impersonates a cellular base station to deliver phishing text messages directly to nearby mobile devices. Messages were injected at the radio frequency layer, bypassing all carrier-side SMS filtering because they never traverse the carrier's messaging infrastructure.

This is a rare confirmed law enforcement action against physical phishing infrastructure. From a defender's perspective, SMS blaster attacks are essentially undetectable by the recipient — the messages appear as ordinary SMS with no anomalous sender attributes. Mobile network operators can detect rogue base stations with IMSI catcher detection systems, but individual users have no practical mitigation beyond skepticism of unsolicited texts requesting credential entry.
