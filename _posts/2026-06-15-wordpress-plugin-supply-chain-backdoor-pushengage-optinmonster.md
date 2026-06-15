---
title: "Trusted WordPress Plugin Scripts Tampered to Plant Hidden Admin Backdoors"
date: 2026-06-15 09:59:38 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, appsec]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html
---

Attackers tampered with trusted JavaScript files used by the WordPress plugins PushEngage, OptinMonster, and TrustPulse, turning them into a supply chain backdoor vector.
When a logged-in site administrator loaded a page containing the tampered script, the code silently created a new admin account under the attacker's control and installed a hidden plugin that maintains persistent access.
Ordinary site visitors did not trigger the malicious behavior.
Site administrators using these plugins should audit their WordPress admin user lists for unrecognized accounts and check for unfamiliar installed plugins.
