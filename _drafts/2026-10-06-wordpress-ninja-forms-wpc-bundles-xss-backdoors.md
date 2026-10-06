---
title: "Ninja Forms and WPC Product Bundles XSS Flaws Exploited to Backdoor WordPress Sites"
date: 2026-10-06 21:00:27 +0000
categories: [Daily Signal]
tags: [xss, wordpress, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ninja-forms-plugin-flaw-exploited-to-hack-wordpress-sites/
---

Attackers are exploiting stored cross-site scripting (XSS) vulnerabilities in
two unrelated WordPress plugins — Ninja Forms and WPC Product Bundles for
WooCommerce — to compromise sites. The injected scripts are being used to
install backdoors and create rogue administrator accounts, giving attackers
persistent access. Because the two plugins are unrelated, this looks like
opportunistic exploitation of multiple vulnerable extensions rather than one
coordinated campaign. Site operators running either plugin should update to
patched versions and audit their admin user list for unauthorized accounts.
