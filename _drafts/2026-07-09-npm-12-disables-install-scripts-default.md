---
title: "npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk"
date: 2026-07-09 16:49:02 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, devsecops, github]
severity: informational
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html
---

GitHub has released npm 12 with install scripts disabled by default, a
change intended to reduce supply chain risk from malicious
postinstall/preinstall scripts. The `allowScripts` setting now defaults to
off, so scripts that previously ran automatically during `npm install` are
now opt-in. GitHub is also deprecating granular access tokens (GATs) that
could previously be used to bypass two-factor authentication requirements.
