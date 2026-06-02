---
title: "Red Hat NPM Supply Chain Attack Compromises 32 Packages via GitHub Account Hijack"
date: 2026-06-02 13:42:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, github]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/
  - name: The Record (Recorded Future)
    url: https://therecord.media/red-hat-removes-tainted-packages-after-software-pipeline-compromise
---

A supply chain attack hit Red Hat's npm ecosystem after attackers compromised a Red Hat GitHub account and used it to push 96 malicious package versions across 32 packages. The injected payload is a credential-stealing worm similar to Mini Shai-Hulud, designed to exfiltrate secrets and propagate through CI/CD pipelines. The affected packages are downloaded approximately 117,000 times per week. Red Hat has removed the tainted packages and is conducting a preliminary investigation into the scope of compromise. Organizations using affected Red Hat npm packages should audit recent installs, rotate all credentials in affected environments, and review CI/CD pipeline logs for signs of lateral movement or persistence.
