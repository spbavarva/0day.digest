---
title: "WordPress Redirect Plugin Hid Dormant Backdoor for Five Years Across 70,000 Sites"
date: 2026-04-29 22:13:15 +0000
categories: [Daily Signal]
tags: [supply-chain, appsec, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/popular-wordpress-redirect-plugin-hid-dormant-backdoor-for-years/
---

The Quick Page/Post Redirect plugin — installed on more than 70,000 WordPress sites — was found to contain a backdoor added approximately five years ago that allows arbitrary code injection into any site running it. The backdoor remained dormant and undetected for years before researchers identified it.

WordPress administrators running this plugin should remove it immediately and audit sites for signs of unauthorized code execution or file modification. This is another instance of long-lived supply-chain backdoors in the WordPress ecosystem, which has seen multiple similar incidents in recent months including the Smart Slider and EssentialPlugin cases. Any site that ran this plugin should be treated as potentially compromised regardless of whether active exploitation has been observed.
