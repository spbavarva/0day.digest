---
title: "AWS STS Simplifies Session Token Size Limits, Adds Monitoring"
date: 2026-09-15 22:21:59 +0000
categories: [Daily Signal]
tags: [aws, iam, cloud-security]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/aws-sts-simplifies-session-token-size-limits-and-adds-session-token-size-monitoring/
---

AWS Security Token Service (STS) replaced its separate packed-policy-
size and overall session-token-size limits with a single unified token
size limit of 4,096 bytes, simplifying session policy and tag sizing
for IAM roles.

STS also now reports session token size in API responses, giving
practitioners visibility to monitor and tune session policies before
hitting the limit.
