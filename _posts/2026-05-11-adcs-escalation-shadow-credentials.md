---
title: "Unit 42 Unpacks AD CS Escalation: Template Misconfigs, Shadow Credentials, and Detection Guidance"
date: 2026-05-11 22:00:43 +0000
categories: [Daily Signal]
tags: [privilege-escalation, iam, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/
---

Unit 42 published a detailed analysis of Active Directory Certificate Services (AD CS) exploitation
covering template misconfigurations and shadow credential abuse as escalation primitives. The post
includes behavioral detection patterns defenders can use to identify AD CS misuse in their
environments.

AD CS escalation techniques (ESC1–ESC8 and beyond) have been a top post-exploitation path in
enterprise environments since the original Certified Pre-Owned research. This update covers newer
tooling and detection evasion techniques. Defenders should cross-reference their AD CS templates
against the misconfiguration catalog and ensure logging is enabled on the Certificate Authority for
certificate request anomalies.
