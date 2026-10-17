---
title: "Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants"
date: 2026-10-17 06:16:46 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach, microsoft]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
---

Threat actors are abusing a single compromised Microsoft 365 credential
belonging to ConnectWise Cloud Backup (formerly SkyKick) to sign into 173
downstream customer M365 tenants. ConnectWise Cloud Backup is used broadly
by managed service providers, making this a one-to-many supply chain
exposure rather than an isolated account compromise.

The campaign is active. Organizations using ConnectWise Cloud Backup /
SkyKick should review M365 sign-in logs for anomalous access tied to the
MSP's service accounts and rotate associated credentials.
