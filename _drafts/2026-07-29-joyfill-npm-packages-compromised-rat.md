---
title: "Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js"
date: 2026-07-29 04:20:57 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
---

Beta and release-candidate versions of two npm packages in the @joyfill
namespace - @joyfill/layouts@0.1.2-2773.beta.0 and
@joyfill/components@4.0.0-rc24-2773-beta.4 - were compromised to deliver a
remote access trojan linked to the DEV#POPPER malware family. The packages
contain an import-time JavaScript implant that resolves and runs encrypted
code as soon as they're imported into a Node.js project. Teams that pinned
to these beta/RC versions should treat any host that imported them as
compromised and rotate credentials reachable from those environments.
