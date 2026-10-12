---
title: "AWS GuardDuty Adds Five New Indicators for Attack Sequence Detection"
date: 2026-10-12 21:58:44 +0000
categories: [Daily Signal]
tags: [aws, cloud-security, cspm]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/guardduty-extended-threat-detection-has-added-five-new-indicators-to-surface-attack-sequences/
---

Amazon GuardDuty Extended Threat Detection added five new indicator types —
MALICIOUS_PACKAGE, MISCONFIGURATION, REACHABILITY, SENSITIVE_DATA, and
VULNERABILITY — used to correlate weaker signals into a single
critical-severity attack sequence finding.

The feature combines these indicators once their composition crosses a
credibility threshold, aiming to surface multi-stage attack sequences
rather than isolated alerts.

No action is required from customers; the new indicators apply
automatically to existing GuardDuty Extended Threat Detection findings.
