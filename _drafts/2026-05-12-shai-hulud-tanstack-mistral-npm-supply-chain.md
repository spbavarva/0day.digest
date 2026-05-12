---
title: "Shai Hulud Worm Returns: Signed Malicious TanStack and Mistral npm Packages Deployed"
date: 2026-05-12 11:29:36 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, pypi, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/
  - name: Dark Reading
    url: https://www.darkreading.com/application-security/worm-redux-fresh-mini-shai-hulud-infections-bite-supply-chain
---

A fresh wave of the Shai Hulud supply chain campaign has compromised hundreds of npm and
PyPI packages tied to the TanStack ecosystem and the Mistral AI library. The packages
arrived cryptographically signed, reducing the chance that automated checks would reject
them at install time. The self-propagating worm—attributed to threat actor TeamPCP—steals
credentials from developer machines after installation. This is a distinct wave from the
April 2026 campaign that targeted Bitwarden and other packages. Developers using TanStack
query, router, or related libraries should immediately audit installed package versions
against the official TanStack registry and look for unexpected patch releases published
during the attack window. Mistral SDK users should do the same. Lock all dependency
versions and re-run installs from a clean cache.
