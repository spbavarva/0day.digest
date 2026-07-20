---
title: "SleeperGem Supply Chain Attack Hits RubyGems Developers"
date: 2026-07-20 05:15:39 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
---

Researchers flagged a new software supply chain attack, codenamed
SleeperGem, targeting the Ruby ecosystem through three malicious
RubyGems packages. One rogue gem, published July 18, was named
git_credential_manager to mimic the legitimate credential manager tool;
a second package named Dendreo was also identified. The gems were
designed to serve additional payloads to developer machines that
installed them. Ruby developers should audit their installed gems for
these package names and remove them if found.
