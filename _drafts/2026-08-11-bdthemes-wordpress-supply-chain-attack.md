---
title: "BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins"
date: 2026-08-11 05:48:44 +0000
categories: [Daily Signal]
tags: [supply-chain, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html
---

A threat actor compromised WordPress plugin vendor BdThemes' upstream
infrastructure and modified a remote JSON feed delivered to administrators'
browsers, using it to create rogue admin accounts on affected sites.

Wordfence researcher Paolo Tresso noted this differs from traditional
supply chain attacks: no source files were modified in the official
WordPress.org repository. The WordPress plugins team temporarily disabled
BdThemes downloads while investigating.
