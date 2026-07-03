---
title: "North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets"
date: 2026-07-03 16:07:15 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html
---

JFrog identified malicious npm packages — "rollup-packages-polyfill-core"
and "rollup-runtime-polyfill-core" — that impersonate the legitimate
"rollup-plugin-polyfill-node" project, copying its description and
repository metadata. The packages are linked to North Korea-affiliated
threat actors and are built to facilitate remote access and steal
developer secrets. Developers should audit dependencies for these exact
package names, verify polyfill packages against the official Rollup
organization, and rotate any credentials exposed on systems where the
packages were installed.
