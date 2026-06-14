---
title: "GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks"
date: 2026-06-11 06:23:03 +0000
categories: [Daily Signal]
tags: [npm, supply-chain, github, devsecops]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
---

GitHub announced that npm version 12 will disable install scripts by default as part of a broader set of breaking changes targeting supply chain attacks.
Install scripts triggered via npm lifecycle hooks during "npm install" have been a common vector for malicious package payloads.
Disabling them by default removes a major automatic code-execution path for compromised or malicious npm packages.
Maintainers and CI pipelines that rely on install scripts for legitimate build steps will need to explicitly opt back in once npm 12 ships.
