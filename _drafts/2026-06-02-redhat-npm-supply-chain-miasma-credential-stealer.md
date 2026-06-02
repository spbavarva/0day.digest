---
title: "Supply Chain Attack Compromises 32 Red Hat npm Packages with Miasma Credential Stealer"
date: 2026-06-01 21:38:29 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, appsec]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/
  - name: SecurityWeek
    url: https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/
---

Attackers compromised more than 30 npm packages under Red Hat's @redhat-cloud-services
namespace and published 96 malicious package versions containing "Miasma," a new variant
of the Shai-Hulud credential-stealing worm. The malware targets developer credentials,
making any CI/CD pipeline that installed the affected packages during the compromise
window potentially exfiltrated.

Developers and organizations using @redhat-cloud-services packages should audit
`package-lock.json` and pipeline logs for installs of malicious versions. Rotate any
credentials that may have been accessible from affected build environments. Red Hat has
been notified; check their advisory for the full list of affected package versions.
