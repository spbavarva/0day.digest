---
title: "Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks"
date: 2026-08-04 13:30:23 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html
---

A credential-stealing, self-propagating npm worm that first appeared in
keyv@6.0.0 spread beyond the Keyv and Cacheable namespaces into hundreds
of packages across multiple maintainer organizations on August 4, 2026.

SafeDep verified 353 poisoned versions across 79 package names, with
monitoring putting the wider footprint at 442 versions across 353 names;
Aikido later reported at least 868 affected packages. The worm has also
been observed planting hooks in Claude Code and VS Code configurations.

Developers who recently installed affected packages should audit
lockfiles, rotate any exposed npm and CI credentials, and check for
unexpected editor hook configurations.
