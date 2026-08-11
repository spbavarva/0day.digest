---
title: "BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins"
date: 2026-08-11 05:48:44 +0000
categories: [Daily Signal]
tags: [supply-chain, wordpress]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html
---

Researchers disclosed a supply chain compromise affecting WordPress plugin
vendor BdThemes, prompting WordPress.org's plugins team to temporarily
disable the vendor's plugin downloads. Unlike typical software supply
chain attacks, no source code files in the official WordPress.org
repository were modified — Wordfence researcher Paolo Tresso said the
attack instead poisoned JSON data to create rogue administrator accounts
on sites running the affected plugins.
