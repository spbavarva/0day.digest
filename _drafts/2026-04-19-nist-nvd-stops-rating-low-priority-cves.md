---
title: "NIST to Stop Rating Non-Priority Flaws as CVE Volume Overwhelms NVD"
date: 2026-04-19 14:17:43 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/nist-to-stop-rating-non-priority-flaws-due-to-volume-increase/
---

NIST will stop assigning CVSS severity scores to lower-priority vulnerabilities in the
National Vulnerability Database, citing an unsustainable rise in CVE submission volumes.
Only higher-priority flaws will continue to receive full NVD analysis and scoring.

This is a significant operational change for vulnerability management programs that depend
on NVD CVSS scores for automated triage, SLA tracking, and compliance reporting. Tools
and workflows that ingest NVD data may begin returning incomplete scoring for a growing
fraction of published CVEs.

Security teams should evaluate their dependency on NVD-sourced CVSS scores and consider
supplementing with vendor-provided advisories or alternative scoring sources such as
FIRST EPSS data to maintain triage coverage.
