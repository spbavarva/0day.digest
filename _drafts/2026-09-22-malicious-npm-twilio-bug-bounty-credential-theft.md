---
title: "Malicious npm Package Poses as Twilio Bug-Bounty Tool to Steal Credentials"
date: 2026-09-22 17:58:15 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/malicious-npm-package-poses-as-twilio.html
---

Researchers disclosed a malicious npm package, "tw-pkgprobe-7731," that
masquerades as a security tool for developers integrating Twilio into their
applications while stealthily harvesting sensitive data.

The package was first uploaded to the npm registry in mid-August 2026 by an
account named "twdepprobe7731." Developers who added Twilio-related
dependencies recently should check their lockfiles for this package.
