---
title: "Funnel Builder WordPress Plugin Exploited for Credit Card Theft"
date: 2026-05-15 19:30:33 +0000
categories: [Daily Signal]
tags: [xss, vulnerability, appsec, wordpress]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/funnel-builder-wordpress-plugin-bug-exploited-to-steal-credit-cards/
---

A critical vulnerability in the Funnel Builder plugin for WordPress is under active exploitation. Attackers are using it to inject malicious JavaScript snippets into WooCommerce checkout pages, enabling real-time credit card skimming from customers completing purchases.

WordPress site owners running Funnel Builder alongside WooCommerce should update the plugin immediately and inspect checkout page markup for unauthorized script injections. Store operators should review recent transaction records for anomalies potentially tied to the skimmer's activity window. The attack pattern mirrors established Magecart-style JavaScript injection targeting e-commerce payment flows.
