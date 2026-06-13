---
title: "npm 12 Will Disable Dependency Install Scripts by Default to Curb Supply Chain Attacks"
date: 2026-06-13 15:52:58 +0000
categories: [Daily Signal]
tags: [npm, supply-chain, devsecops]
severity: informational
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
---

npm 12 will change the default behavior of `npm install`: lifecycle scripts
(such as `preinstall`, `install`, and `postinstall`) from dependencies will no
longer run automatically unless a project explicitly allows them.

Malicious install scripts have been a common technique in npm supply chain
attacks, letting a compromised package run arbitrary code the moment it is
installed.

Projects that rely on install scripts for legitimate build steps will need to
opt in once npm 12 ships.
