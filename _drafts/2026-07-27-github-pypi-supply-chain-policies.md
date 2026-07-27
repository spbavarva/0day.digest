---
title: "New GitHub, PyPI Policies Boost Supply Chain Security"
date: 2026-07-27 14:26:00 +0000
categories: [Daily Signal]
tags: [supply-chain, github, pypi]
severity: informational
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/new-github-pypi-policies-boost-supply-chain-security/
---

GitHub and PyPI have rolled out new supply-chain protections aimed at
limiting the window for poisoned-package attacks. Dependabot now waits three
days after a package release before opening an automated pull request,
giving time for malicious releases to be caught before adoption. PyPI will
reject file uploads to releases older than 14 days, closing a path attackers
have used to slip malicious files into existing, trusted releases.
Maintainers can still adjust the Dependabot cooldown window via
dependabot.yml.
