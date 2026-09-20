---
title: "Malicious npm Packages Evade Install-Script Defenses at Runtime"
date: 2026-09-20 14:11:21 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/
---

An ongoing npm malware campaign centered on the `indexed-btree` package
hides malicious code in the package's normal runtime behavior instead of
its install scripts. This lets it slip past supply-chain tooling that
only inspects install-time hooks for malicious activity.

The technique underscores a blind spot in defenses that focus solely on
install scripts. Teams should extend dependency scanning to runtime code
paths, not just install hooks, and review any recent pulls of this
package.
