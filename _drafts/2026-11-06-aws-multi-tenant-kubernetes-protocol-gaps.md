---
title: "AWS Details Protocol Security Gaps in Multi-Tenant Kubernetes"
date: 2026-11-06 21:08:50 +0000
categories: [Daily Signal]
tags: [kubernetes, container-security, cloud-security, aws]
severity: medium
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/addressing-protocol-security-gaps-in-multi-tenant-kubernetes/
---

AWS highlighted that protocols like Android Debug Bridge (ADB) and
WebRTC default to unencrypted channels and don't support enterprise
auth mechanisms like JWTs. In a multi-tenant Kubernetes cluster,
including Amazon EKS, pods can reach other tenants' open ports by
default unless network policies are explicitly configured.

Teams running multi-tenant clusters should audit for services using
these protocols and enforce network policies to prevent cross-tenant
access.
