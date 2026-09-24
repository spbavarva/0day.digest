---
title: "Exposed GitLab Project Email Addresses Let Attackers Push Code"
date: 2026-09-24 17:47:44 +0000
categories: [Daily Signal]
tags: [gitlab, appsec, supply-chain]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/exposed-gitlab-project-email-addresses-let-attackers-push-code/
---

Private GitLab project email addresses — used to let contributors push
issues or tasks to a project via email — are being deliberately exposed
in READMEs, contributing guides, and support pages that collect bug
reports.

Because these addresses can be used to push content into a project,
exposing them lets attackers submit code or issues without going through
normal access controls.

Maintainers should treat these project-specific email addresses as
sensitive credentials and avoid publishing them in public documentation.
