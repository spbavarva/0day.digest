---
title: "PCPJack Worm Evicts Rival Malware and Steals AWS and Kubernetes Credentials"
date: 2026-05-08 08:32:34 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, aws, kubernetes, container-security]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/
---

The PCPJack malware framework targets web applications and cloud environments, removing competing
TeamPCP infections to claim exclusive control over compromised hosts before stealing credentials
for AWS, Docker, and Kubernetes deployments. The evict-and-replace behavior signals a sophisticated
threat actor maximizing return on access. Cloud credential theft from these environments enables
lateral movement across cloud infrastructure and potential supply chain impact. Organizations running
public-facing web apps in cloud environments should audit for unexpected processes and review IAM
key rotation policies.
