---
title: "CISA Contractor Exposes AWS GovCloud Keys on Public GitHub"
date: 2026-05-22 16:34:24 +0000
categories: [Daily Signal]
tags: [data-breach, cloud-security, aws, iam]
severity: critical
must_know: true
sources:
  - name: Krebs on Security
    url: https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/
---

A CISA contractor intentionally published AWS GovCloud credentials and a wide range of other agency secrets to a public GitHub repository. CISA is still working to invalidate the leaked credentials and contain the breach. Lawmakers in both the House and Senate are demanding answers. The incident affects GovCloud environments tied to federal infrastructure — any downstream systems or services relying on those credentials must be treated as compromised until full rotation is confirmed.
