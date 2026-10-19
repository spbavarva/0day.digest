---
title: "ConnectWise Suspends Cloud Backup After Supply Chain Attack"
date: 2026-10-19 19:45:00 +0000
categories: [Daily Signal]
tags: [supply-chain, cloud-security, data-breach]
severity: critical
must_know: true
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/connectwise-suspends-cloud-backup-service-supply-chain-attack
  - name: Dark Reading
    url: https://www.darkreading.com/identity-access-management-security/connectwise-disables-cloud-backups-downstream-msps
  - name: SecurityWeek
    url: https://www.securityweek.com/connectwise-suspends-cloud-services-in-response-to-cyberattack/
---

ConnectWise confirmed unauthorized access to its Cloud Backup environment
and suspended the service as a precaution. Researchers say attackers used
stolen ConnectWise credentials to authenticate into customers' Microsoft 365
tenants; ConnectWise says the scope of customer impact remains unconfirmed.

ConnectWise's RMM and backup tools are widely used by MSPs, making this a
supply chain risk for any organization relying on an affected MSP.
Administrators should rotate ConnectWise-linked credentials and review M365
sign-in logs for anomalous activity.
