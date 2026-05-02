---
title: "ConsentFix v3 Automates OAuth Consent Abuse Against Azure Tenants"
date: 2026-05-02 14:32:25 +0000
categories: [Daily Signal]
tags: [azure, iam, cloud-security, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/consentfix-v3-attacks-target-azure-with-automated-oauth-abuse/
---

ConsentFix v3, circulating on hacker forums, builds on earlier OAuth consent-phishing techniques by adding automation to scale attacks against Azure tenants. The tooling streamlines the process of tricking users into granting persistent OAuth permissions to attacker-controlled applications — effectively creating a backdoor that survives password resets.

The automation differentiates this iteration from previous manual-phishing variants, lowering the skill threshold and increasing campaign throughput. Azure defenders should audit Conditional Access policies to restrict app consent grants, enforce admin consent for third-party OAuth applications, and review the enterprise app registrations for unexpected permissions. Microsoft Identity Protection logs should be monitored for anomalous OAuth grant activity.
