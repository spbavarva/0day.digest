---
title: "AWS Adds IAM Outbound Identity Federation for Cross-Partition Access"
date: 2026-11-09 16:08:30 +0000
categories: [Daily Signal]
tags: [aws, cloud-security, iam]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/simplify-cross-partition-access-with-aws-iam-outbound-identity-federation/
---

AWS now supports using IAM outbound identity federation tokens to
assume roles in other AWS partitions, such as Commercial, China,
GovCloud (US), and the European Sovereign Cloud.

Previously, workloads spanning multiple partitions needed separate
credential management per partition. Outbound federation lets a
workload in one partition assume a role in another without
provisioning long-lived cross-partition credentials.

Teams running multi-partition AWS workloads should evaluate this as a
way to reduce standing cross-partition credentials.
