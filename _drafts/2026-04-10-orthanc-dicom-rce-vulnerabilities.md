---
title: "Orthanc DICOM Server Vulnerabilities Enable RCE in Medical Imaging Systems"
date: 2026-04-10 11:53:45 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/orthanc-dicom-vulnerabilities-lead-to-crashes-rce/
---

Multiple vulnerabilities in Orthanc, a widely-used open-source DICOM server for
medical imaging, can be exploited for denial-of-service, information disclosure, and
arbitrary code execution. Orthanc is deployed in hospitals and radiology departments
globally to store, manage, and serve DICOM images. Exploitation could expose sensitive
patient imaging data and disrupt clinical operations. Healthcare organizations running
Orthanc instances should apply available patches immediately and audit network exposure
of their DICOM infrastructure. Medical imaging servers are frequently under-monitored
and run on unpatched software due to clinical continuity constraints.
