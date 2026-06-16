---
title: "GhostTree: Recursive NTFS Junctions Force Microsoft Defender Folder Scans to Never Complete"
date: 2026-06-16 14:17:00 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ghosttree-attack-abused-recursive-windows-junctions-to-hide-malware/
---

Varonis researchers published GhostTree, a technique that creates recursive NTFS junction points to generate a theoretically infinite number of valid Windows file paths. When Microsoft Defender attempts a folder scan over the recursive tree, the scan runs indefinitely without completing, leaving malware nested inside the junction structure undetected. Setting up the junctions does not require elevated privileges. Organizations should test Defender's behavior against known deep junction trees and add junction creation as an anomaly detection signal in filesystem-behavior tooling; supplementary AV or EDR solutions not dependent on recursive path traversal provide an alternative detection layer.
