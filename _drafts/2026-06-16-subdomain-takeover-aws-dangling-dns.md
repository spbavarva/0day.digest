---
title: "AWS Threat Tactic Spotlight: Detecting and Preventing Subdomain Takeover via Dangling DNS"
date: 2026-06-16 17:53:00 +0000
categories: [Daily Signal]
tags: [cloud-security, aws]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
---

AWS published a practitioner guide on subdomain takeover—an attack where threat actors register abandoned cloud resources still pointed to by live DNS entries in a victim's zone, allowing them to serve content under the victim's domain. Attackers use squatted resources to host phishing pages, intercept cookie-scoped session tokens, or hijack OAuth flows. The post covers detection patterns and AWS-native mitigations including Route 53 monitoring, S3 and CloudFront configuration audits, and AWS Config rules for identifying dangling CNAMEs. Teams managing large or legacy DNS estates should audit for CNAMEs pointing to deprovisioned AWS services as a routine hygiene step.
