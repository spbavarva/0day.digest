---
title: "Default Azure Automation Setting Enables Cross-Tenant Identity Takeover"
date: 2026-07-24 12:48:16 +0000
categories: [Daily Signal]
tags: [azure, cloud-security, iam, privilege-escalation]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cloud-security/default-azure-automation-setting-cross-tenant-identity-takeover
---

Microsoft has fixed a public-by-default configuration in Azure Automation
that, combined with a chain of code flaws, could have let an attacker
seize another tenant's identity and gain access to that tenant's data,
credentials, and cloud workloads. Azure customers using Automation
runbooks should confirm they're on the corrected configuration and review
runbook permissions for unintended cross-tenant exposure.
