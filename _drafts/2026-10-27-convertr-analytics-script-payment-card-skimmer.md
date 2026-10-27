---
title: "Compromised Convertr Analytics Script Used to Steal Payment Card Data"
date: 2026-10-27 20:57:25 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-hijack-convertr-analytics-script-to-steal-payment-card-data/
---

A credit card skimming group compromised a shared analytics script used
by e-commerce platform Convertr, and used it to harvest shoppers' payment
card data during checkout on affected sites.

Because the script is shared across merchants using Convertr's analytics
tooling, this is a supply-chain-style skimming attack rather than a
single-site breach. Site operators using Convertr should audit for
unauthorized script modifications and review checkout page integrity.
