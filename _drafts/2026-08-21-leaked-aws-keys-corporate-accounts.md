---
title: "Hundreds of Leaked AWS Keys Give Full Control Over Corporate Accounts"
date: 2026-08-21 15:55:15 +0000
categories: [Daily Signal]
tags: [aws, iam, cloud-security, data-breach]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hundreds-of-leaked-aws-keys-give-full-control-over-corporate-accounts/
---

More than 9,300 AWS access keys publicly exposed between August 2022 and
August 2026 are still active and valid. The keys give attackers full control
over the affected corporate accounts, and the multi-year exposure window
suggests many organizations never rotated credentials after leaking them.
Teams should audit for publicly exposed keys (source repos, CI logs,
container images) and rotate any long-lived AWS credentials as a matter of
routine, not just after a known incident.
