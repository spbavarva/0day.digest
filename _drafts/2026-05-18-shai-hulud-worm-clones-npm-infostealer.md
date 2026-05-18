---
title: "Four Malicious npm Packages Deliver Infostealers and Shai-Hulud Worm Clones"
date: 2026-05-18 08:57:26 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html
---

Researchers discovered four malicious npm packages delivering information-stealing malware and a
Phantom Bot DDoS component: `chalk-tempalte`, `@deadcode09284814/axios-util`, `axois-utils`, and
`color-style-utils`. One package is a clone of the Shai-Hulud worm open-sourced by TeamPCP, showing
threat actors are actively adapting the publicly released code for new npm-based campaigns.

Combined downloads across the four packages totaled roughly 3,000 before removal. Developers should
audit `package.json` files and build logs for any of these package names. This continues the broader
TeamPCP/Shai-Hulud supply chain campaign; teams that track that threat actor should update their IOC
sets accordingly.
