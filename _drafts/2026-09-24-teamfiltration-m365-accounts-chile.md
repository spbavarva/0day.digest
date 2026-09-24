---
title: "TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords"
date: 2026-09-24 06:32:03 +0000
categories: [Daily Signal]
tags: [microsoft, cloud-security, iam]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html
---

Proofpoint disclosed an active TeamFiltration campaign, tracked as
UNK_CondorFiltration, that targeted over 5,700 Microsoft 365 accounts
across 28 tenants, primarily in Chilean retail and financial
institutions.

The campaign originated from 1,487 unique AWS EC2 source IP addresses
and successfully compromised seven accounts, reportedly by exploiting
default passwords.

Organizations should enforce password rotation on new accounts and
monitor for authentication attempts from AWS-hosted IP ranges at unusual
volume.
