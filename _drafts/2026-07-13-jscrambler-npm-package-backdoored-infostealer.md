---
title: "Hackers Backdoor Jscrambler npm Package With Infostealer Malware"
date: 2026-07-13 19:44:19 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/
---

A threat actor published a malicious version of Jscrambler's npm package,
backdooring it with infostealer malware before it was pulled. The
compromised package had been downloaded almost 1,500 times. Jscrambler
provides client-side web security tooling, making this a supply chain
compromise of a security-adjacent dependency. Teams that recently
installed Jscrambler via npm should audit for the malicious version and
rotate any credentials that may have been exposed.
