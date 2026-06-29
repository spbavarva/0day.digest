---
title: "Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer"
date: 2026-06-29 05:36:06 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html
---

Researchers at JFrog uncovered two hijacked npm packages and a cluster of Go
packages modified to deploy a Python-based information stealer on Windows,
Linux, and macOS hosts. The malicious packages use VS Code task
configurations to execute the payload, avoiding npm lifecycle-script
execution paths — possibly to stay compatible with npm v12's lifecycle-script
hardening. The campaign spans both the npm and Go ecosystems, indicating a
multi-ecosystem supply chain attack. Developers should audit recently added
VS Code tasks in dependencies and check lockfiles against published IOCs.
