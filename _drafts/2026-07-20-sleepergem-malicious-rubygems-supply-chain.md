---
title: "SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines"
date: 2026-07-20 05:15:39 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
---

Researchers identified a software supply chain attack, dubbed SleeperGem,
targeting the Ruby ecosystem through three malicious RubyGems packages
published to serve additional payloads onto developer machines. The rogue
gems include versions of a package named "git_credential_manager" (2.8.0
through 2.8.3, published July 18, 2026) and "Dendreo" (1.1.3, 1.1.4). The
git_credential_manager name mimics the legitimate Microsoft tool of the
same name, raising typosquatting risk. Ruby developers should audit
installed gems against these version numbers and remove any matches
immediately.
