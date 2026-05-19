---
title: "Mini Shai-Hulud Campaign Poisons AntV npm Packages via Compromised Maintainer Account"
date: 2026-05-19 04:54:17 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, credential-stealer]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html
---

The ongoing Mini Shai-Hulud attack campaign has compromised npm packages in the
`@antv` ecosystem by taking over the `atool` maintainer account. The attack
targets `echarts-for-react`, a React wrapper for Apache ECharts with roughly
1.1 million weekly downloads, along with other packages tied to the same
maintainer.

This is part of a broader pattern of compromised-maintainer-account attacks
across the npm ecosystem. Developers using affected `@antv` packages should
check their installed versions, audit recent package updates, and rotate any
secrets accessible from their build environments. Lock files should be
committed and integrity hashes verified on install.
