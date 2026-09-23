---
title: "How One Kubernetes YAML Can Hand Over a GCP Organization"
date: 2026-09-23 14:01:11 +0000
categories: [Daily Signal]
tags: [kubernetes, privilege-escalation, gcp, cloud-security]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/
---

Varonis researchers demonstrated how a Kubernetes user with limited
permissions can potentially gain control of an entire Google Cloud
organization by exploiting the authority granted to Google Kubernetes
Config Connector. The issue is a confused-deputy problem: Config
Connector's own elevated GCP permissions can be leveraged through a
single crafted Kubernetes YAML file.

Organizations using Config Connector should review the IAM bindings
granted to it and restrict who can apply Config Connector resources.
