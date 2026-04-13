---
title: "OpenAI Rotates macOS Code-Signing Certs After North Korea-Linked Axios Supply Chain Attack"
date: 2026-04-13 17:39:10 +0000
categories: [Daily Signal]
tags: [supply-chain, openai, malware, github]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/openai-rotates-macos-certs-after-axios-attack-hit-code-signing-workflow/
  - name: SecurityWeek
    url: https://www.securityweek.com/openai-impacted-by-north-korea-linked-axios-supply-chain-hack/
---

OpenAI is rotating macOS code-signing certificates after a GitHub Actions workflow executed
a malicious Axios npm package during a North Korea-linked supply chain attack, potentially
exposing the certificates. The incident is an extension of the broader Axios infrastructure
compromise reported earlier this month.

Exposure of code-signing certificates could enable distribution of malicious binaries
appearing to originate from OpenAI. OpenAI has confirmed the issue and is taking corrective
action. SecurityWeek attributes the Axios compromise to North Korean threat actors, consistent
with known DPRK interest in developer toolchain infiltration.

Organizations using Axios-dependent tooling in CI/CD pipelines should audit npm dependency
chains, review GitHub Actions execution logs for unexpected package resolutions, and rotate
any secrets that may have been accessible during affected workflow runs.
