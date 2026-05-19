---
title: "GitHub Actions Supply Chain Attack Redirects All Tags to Credential-Stealing Commit"
date: 2026-05-19 05:28:06 +0000
categories: [Daily Signal]
tags: [supply-chain, github, ci-cd, malware, credential-stealer]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html
---

Threat actors compromised the `actions-cool/issues-helper` GitHub Actions
workflow, redirecting every existing tag to point to a malicious imposter
commit that exfiltrates CI/CD credentials to an attacker-controlled server.
The tampered commit does not appear in the action's normal commit history,
making it difficult to detect through standard audit review.

Any pipeline referencing this action by tag (rather than pinned SHA) will have
executed the malicious code and should treat its CI secrets as compromised.
Organizations should pin all third-party Actions to full commit SHAs, audit
workflow logs for unexpected outbound connections, and rotate any secrets
exposed in affected pipelines immediately.
