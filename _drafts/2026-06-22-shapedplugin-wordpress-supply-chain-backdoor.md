---
title: "ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack"
date: 2026-06-22 18:00:48 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, appsec]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html
---

Multiple ShapedPlugin WordPress Pro plugins were compromised in a supply chain attack after threat actors tampered with the vendor's official release channels. According to Wordfence, attackers compromised ShapedPlugin's build and distribution pipeline and injected backdoor code into Pro plugin releases pushed through official licensed update channels. Sites that received updates during the compromise window should treat them as untrusted and audit for backdoor indicators rather than assuming official-channel updates are safe by default.
