---
title: "pydicom/pynetdicom Path Traversal Flaw Allows Unauthenticated Arbitrary File Writes"
date: 2026-06-25 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, ics, pypi]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-176-01
---

CISA disclosed a path traversal vulnerability (CVSS 9.1) in pynetdicom
versions ≥1.0.0 and <3.0.4 that lets an unauthenticated attacker write to
arbitrary file paths on the host. pydicom/pynetdicom is a widely used
open-source Python toolkit for DICOM medical imaging, deployed across
healthcare imaging pipelines worldwide. A fix is available in v3.0.4 —
organizations running pynetdicom-based imaging integrations should update
promptly.
