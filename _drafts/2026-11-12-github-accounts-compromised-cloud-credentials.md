---
title: "Hackers Compromise 4,800 GitHub Accounts to Steal Cloud Credentials"
date: 2026-11-12 22:25:30 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/
---

A campaign dubbed "wfx-loot" used 4,837 compromised GitHub accounts to
probe 61,764 repositories, open pull requests, and push secrets-stealing
malware designed to harvest cloud credentials. A related report on the
same campaign puts the CI secret stealer's direct reach at over 1,800
repositories.

Developers should review recent PR activity on their repositories, rotate
any credentials that may have been exposed through affected workflows, and
enforce 2FA on GitHub accounts to prevent further account takeovers.
