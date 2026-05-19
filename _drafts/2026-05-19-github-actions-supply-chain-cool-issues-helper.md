---
title: "GitHub Actions Supply Chain Attack Hijacks actions-cool/issues-helper Tags"
date: 2026-05-19 05:28:06 +0000
categories: [Daily Signal]
tags: [supply-chain, github, credential-theft, devsecops]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html
---

Threat actors compromised the popular GitHub Actions workflow `actions-cool/issues-helper`, redirecting every existing tag to a malicious imposter commit absent from the project's normal commit history.
The malicious code harvests sensitive CI/CD credentials and exfiltrates them to an attacker-controlled server.
Any pipeline referencing this action by tag — rather than a pinned commit SHA — will have executed the payload during the window of compromise.
This is a textbook tag-poisoning supply chain attack: downstream consumers trusted the tag but received attacker-controlled code.
Immediate actions: audit all workflows for `actions-cool/issues-helper` references, rotate any secrets accessible from affected runners, and pin all third-party actions to full commit SHAs going forward.
