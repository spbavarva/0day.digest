---
title: "Malicious npm Package 'indexed-btree' Racks Up Millions of Downloads"
date: 2026-09-22 11:33:59 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/malicious-b-tree-npm-package-accumulates-millions-of-downloads/
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html
---

A malicious npm package named "indexed-btree" has accumulated millions of
downloads while posing as the legitimate "sorted-btree" package, an
ordinary B-tree/indexing utility.

Rather than relying on npm lifecycle scripts, the package hides its malware
trigger inside a prototype method in application runtime code. Researchers
say this reflects a shift in attacker tactics in response to recent
supply-chain security controls that specifically target lifecycle scripts.
