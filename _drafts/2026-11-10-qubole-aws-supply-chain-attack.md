---
title: "Qubole AWS IAM Compromise Triggers Supply Chain Attack"
date: 2026-11-10 13:27:44 +0000
categories: [Daily Signal]
tags: [supply-chain, aws, iam, cloud-security]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/over-a-dozen-organizations-hit-in-qubole-supply-chain-attack/
---

Attackers used compromised IAM credentials belonging to the Qubole big
data platform's AWS account to breach and exfiltrate data from more than
a dozen downstream customers' AWS environments. Stolen data includes
customer files, secrets, keys, environment variables, and credentials.
The incident highlights the risk of third-party SaaS platforms holding
standing AWS access into customer accounts. Organizations using Qubole
should rotate any credentials or secrets that may have been exposed to
the platform.
