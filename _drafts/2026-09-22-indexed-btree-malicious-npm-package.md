---
title: "Malicious npm Package 'indexed-btree' Impersonates sorted-btree, Hides Loader in Runtime Code"
date: 2026-09-22 09:38:18 +0000
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

A malicious npm package named "indexed-btree" posed as the legitimate
sorted-btree indexing utility and accumulated millions of downloads.

Checkmarx researchers found the package hides its malicious loader inside
a prototype method in application runtime code, rather than using npm
lifecycle install scripts — a shift likely aimed at evading tooling that
watches for script-based supply chain attacks. The package has since been
removed from the registry.
