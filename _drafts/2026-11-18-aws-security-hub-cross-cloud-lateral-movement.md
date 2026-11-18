---
title: "AWS Details Detection for Cross-Cloud Lateral Movement via Federated Identity"
date: 2026-11-18 22:28:45 +0000
categories: [Daily Signal]
tags: [cloud-security, aws, privilege-escalation]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/detecting-cross-cloud-lateral-movement-with-aws-security-hub/
---

AWS published guidance on detecting attackers who compromise an identity in
one cloud provider and pivot into a second provider through a federated trust
relationship. The post argues the needed signals already exist but are
scattered across providers.

The guidance walks through correlating those signals using AWS Security Hub.
It's most relevant to teams running multicloud environments with federated
identity trust between providers.
