---
title: "node-ipc npm Package Compromised in Supply Chain Attack to Steal Credentials"
date: 2026-05-15 17:10:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, appsec, devsecops]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/popular-node-ipc-npm-package-compromised-to-steal-credentials/
---

Attackers injected credential-stealing malware into newly published versions of node-ipc, a popular Node.js inter-process communication package on npm. Any developer or CI pipeline that installed the compromised versions should assume credential exposure. This is at least the third significant npm supply chain compromise in recent weeks — following TanStack and Bitwarden — suggesting an organized campaign targeting the npm ecosystem, potentially linked to TeamPCP's Shai-Hulud tooling. Developers should immediately pin or audit node-ipc in their dependency trees, rotate all credentials accessible from affected build environments, and review recently updated packages for signs of tampering.
