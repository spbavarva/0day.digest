---
title: "Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs"
date: 2026-07-09 18:38:49 +0000
categories: [Daily Signal]
tags: [github, appsec, datadog]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html
---

Datadog Security Labs is tracking several overlapping campaigns
systematically enumerating corporate GitHub organizations, repositories,
and user accounts via the GitHub API. Operators use automated scraping
tools with legitimate-sounding user agents, years-old dormant "ghost"
GitHub accounts, and compromised OAuth or personal access tokens to blend
in with normal API traffic while mapping corporate org structure. The
activity appears aimed at building targeting data for follow-on attacks
rather than direct compromise.
