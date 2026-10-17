---
title: "ConnectWise Cloud Backup Breach Exposes 173 Microsoft 365 Tenants"
date: 2026-10-17 15:18:51 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach, cloud-security, microsoft]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
---

Threat actors abused a compromised Microsoft 365 credential belonging to
ConnectWise Cloud Backup (formerly SkyKick Cloud Backup) to sign into 173
customers' M365 tenants. The attackers leveraged application identities tied
to the backup service to gain unauthorized access across multiple
organizations' environments. ConnectWise has shut down customer access to
Cloud Backup while it investigates. Because ConnectWise's tooling is widely
used by MSPs, this is a supply-chain-style compromise rather than an isolated
credential theft. Affected MSPs and downstream customers should review M365
sign-in logs and application consent grants tied to ConnectWise integrations.
