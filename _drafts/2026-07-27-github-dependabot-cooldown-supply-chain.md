---
title: "GitHub Adds 3-Day Dependabot Cooldown to Limit Poisoned Package Adoption"
date: 2026-07-27 08:01:23 +0000
categories: [Daily Signal]
tags: [supply-chain, github, devsecops]
severity: informational
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html
---

GitHub has added a cooldown feature to Dependabot that delays pull requests
for new package releases by at least three days by default, aimed at
reducing automatic adoption of newly published (and potentially poisoned)
package versions. The cooldown option in `dependabot.yml` still lets
maintainers configure a different window. The change targets a known
supply-chain risk pattern: malicious package updates that get pulled into
projects by automated dependency bots before they can be flagged and pulled
from the registry.
