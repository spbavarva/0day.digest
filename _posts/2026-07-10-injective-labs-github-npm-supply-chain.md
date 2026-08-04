---
title: "Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Package"
date: 2026-07-10 17:29:28 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, github, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html
---

Unknown attackers compromised the GitHub repository for Injective Labs'
SDK project and used the access to publish a malicious version of the
`@injectivelabs/sdk-ts` npm package. The compromised release, version
1.20.21, embedded fake telemetry functionality that exfiltrated data from
cryptocurrency wallets, including private keys and mnemonic seed phrases.
Projects that pulled the poisoned package during the compromise window may
have exposed wallet secrets to the attackers. Teams depending on this SDK
should audit lockfiles for the affected version, rotate any wallet keys
that may have been exposed, and pin to a verified clean release.
