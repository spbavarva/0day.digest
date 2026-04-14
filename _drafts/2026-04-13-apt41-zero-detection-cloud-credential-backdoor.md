---
title: "APT41 Deploys Zero-Detection Backdoor to Harvest Cloud Credentials via Typosquatting C2"
date: 2026-04-13 15:08:12 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, iam, data-breach]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cloud-security/apt41-zero-detection-backdoor-harvest-cloud-credentials
---

China-backed APT41 is targeting AWS, Google Cloud, Azure, and Alibaba cloud environments
with a backdoor engineered to harvest cloud credentials. The group uses typosquatting to
disguise command-and-control communication as traffic to legitimate cloud provider domains,
causing it to evade current network detection signatures.

The backdoor is described as achieving near-zero detection across current endpoint and
network security tooling. Cloud credentials obtained by APT41 can enable persistent
multi-cloud lateral movement. Organizations should enforce short-lived credential rotation
with automated expiry, monitor for API calls originating from unexpected regions or service
principals, and audit IAM roles for over-permissive access — particularly cross-account or
cross-cloud trust relationships.
