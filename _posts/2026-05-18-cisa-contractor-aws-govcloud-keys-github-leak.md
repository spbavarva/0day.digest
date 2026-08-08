---
title: "CISA Contractor Exposed AWS GovCloud Keys and Internal System Details on Public GitHub"
date: 2026-05-18 20:48:21 +0000
categories: [Daily Signal]
tags: [data-breach, aws, iam, github, cloud-security, cve]
severity: critical
must_know: true
sources:
  - name: Krebs on Security
    url: https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/
---

A CISA contractor maintained a public GitHub repository exposing credentials
for multiple highly privileged AWS GovCloud accounts alongside detailed
internal documentation on how CISA builds, tests, and deploys its software.
Security researchers who discovered the repository described it as one of the
most egregious government data leaks in recent history.

The exposure was remediated as of last weekend. AWS GovCloud accounts hold
sensitive government workloads; compromised credentials at this level could
have enabled access to classified or law-enforcement-sensitive systems. CISA
organizations relying on shared contractor repos should audit GitHub for
accidental secret commits immediately and rotate any credentials that touched
public repositories.
