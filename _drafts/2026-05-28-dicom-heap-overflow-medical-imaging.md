---
title: "DICOM, Pydicom, GDCM, Orthanc: Heap Overflow via Medical Imaging Format"
date: 2026-05-28 10:00:52 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, appsec]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/
---

Cisco Talos published a technical white paper demonstrating heap overflow vulnerabilities created by exploiting the DICOM medical imaging file format, covering the Pydicom library, GDCM toolkit, and Orthanc DICOM server. The paper provides a concrete case study of how DICOM's flexible structure can be abused to corrupt heap allocations. Healthcare organizations, medical device manufacturers, and radiology software vendors processing DICOM files in production should review their exposure to these libraries and apply available mitigations. The research establishes a clear exploitation primitive — organizations should prioritize patching any internet-exposed DICOM endpoints.
