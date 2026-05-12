---
title: "Official Checkmarx Jenkins AST Plugin Backdoored with Infostealer"
date: 2026-05-11 22:03:06 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, appsec, devsecops, github]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/
---

A rogue version of the Checkmarx Application Security Testing (AST) Jenkins plugin was published to
the Jenkins Marketplace over the weekend. The compromised package contained an infostealer payload,
meaning any CI/CD pipeline that installed the malicious version may have had credentials, secrets,
and build environment data exfiltrated.

Checkmarx issued a warning and organizations should immediately verify which version of the plugin
is installed, rotate any secrets accessible from affected Jenkins agents, and audit job logs for
anomalous outbound connections. This attack is particularly targeted: it hits security teams
performing SAST scans, where the compromised tool has broad read access to source code and
credentials in the build environment.
