---
title: "Microsoft Patches CVSS 10.0 Azure AI Foundry Privilege Escalation Flaw"
date: 2026-09-18 12:47:04 +0000
categories: [Daily Signal]
tags: [azure, microsoft, cve, privilege-escalation, vulnerability]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
---

Microsoft fixed a maximum-severity flaw in Azure AI Foundry, tracked as
CVE-2026-85889 with a CVSS score of 10.0. The issue is a missing
authentication check for a critical function that allowed an unauthorized
network attacker to elevate privileges. Microsoft says no customer action
is required — the fix was applied server-side.
