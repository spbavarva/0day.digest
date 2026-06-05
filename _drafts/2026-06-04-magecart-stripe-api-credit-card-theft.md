---
title: "Magecart Campaign Abuses Stripe API to Host Skimmer Payload and Exfiltrate Stolen Cards"
date: 2026-06-04 20:47:16 +0000
categories: [Daily Signal]
tags: [malware, appsec, data-breach]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/credit-card-theft-campaign-abuses-stripe-to-host-stolen-payment-info/
---

A new Magecart campaign is using Stripe's API infrastructure to both host the
card-skimming JavaScript payload and receive exfiltrated payment data from compromised
checkout pages. Routing through Stripe's legitimate and widely trusted API domain makes
detection by network controls significantly harder than traditional C2 exfil. E-commerce
operators should enforce subresource integrity (SRI) on all third-party checkout scripts,
monitor their Stripe accounts for unauthorized API key activity, and conduct regular
integrity checks on checkout page DOM.
