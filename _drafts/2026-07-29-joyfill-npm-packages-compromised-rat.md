---
title: "Compromised joyfill npm Packages Deploy RAT on Import"
date: 2026-07-29 04:20:57 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
---

Beta release versions of two npm packages in the @joyfill namespace —
@joyfill/layouts and @joyfill/components — were compromised to deliver a
remote access trojan associated with the DEV#POPPER malware family. The
packages contain an import-time JavaScript implant that resolves and runs
encrypted code as soon as they're imported into a Node.js project. Affected
versions include @joyfill/layouts@0.1.2-2773.beta.0 and
@joyfill/components@4.0.0-rc24-2773-beta.4. Teams that installed these beta
releases should treat any host that imported them as compromised and rotate
credentials accessible from that environment.
