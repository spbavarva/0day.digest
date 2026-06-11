---
title: "GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks"
date: 2026-06-11 06:23:03 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, github, devsecops]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
---

GitHub announced breaking changes coming in npm v12, including disabling install scripts (lifecycle hooks like preinstall/postinstall) by default.
The change targets a common supply chain attack technique where malicious packages use these hooks to automatically execute code during `npm install`.
This follows a string of recent npm-targeted campaigns, including Shai-Hulud/Miasma.
Maintainers who legitimately rely on install scripts for build steps will need to explicitly opt back in once the change ships.
