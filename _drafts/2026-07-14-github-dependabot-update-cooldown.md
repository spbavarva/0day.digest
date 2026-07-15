---
title: "GitHub Dependabot Adds Default Cooldown to Curb Supply Chain Risk"
date: 2026-07-14 22:43:35 +0000
categories: [Daily Signal]
tags: [supply-chain, github, devsecops]
severity: informational
must_know: false
sources:
  - name: Simon Willison (quoting GitHub Changelog)
    url: https://simonwillison.net/2026/Jul/14/github-changeling/#atom-everything
---

GitHub's Dependabot now waits at least three days after a new package release
before opening a version-update pull request. The cooldown is enabled by
default and requires no configuration.

The delay gives maintainers a window to catch malicious or broken releases
before they propagate into automated dependency-update PRs, mitigating
supply chain attacks that ride newly published package versions.
