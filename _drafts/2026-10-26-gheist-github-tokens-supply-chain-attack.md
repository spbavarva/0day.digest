---
title: "'Gheist' Campaign Weaponizes Stolen GitHub Tokens to Steal Repo Secrets"
date: 2026-10-26 07:49:46 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/gheist-stolen-github-tokens-cloud-secrets
---

An automated campaign dubbed "Gheist" is using stolen GitHub tokens to plant
workflows that print a repository's secrets into its GitHub Actions logs.
Attackers then download the logs and delete the workflow runs before
GitHub's safeguards can intervene.

The attacks have succeeded against private repositories and GitHub
Enterprise environments, according to an analysis by cloud security company
Wiz. Organizations should audit GitHub Actions workflow permissions and
rotate any tokens with write access to CI/CD pipelines.
