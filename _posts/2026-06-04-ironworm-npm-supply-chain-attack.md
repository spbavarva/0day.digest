---
title: "Rust-Written IronWorm Malware Hits NPM in Credential-Propagating Supply Chain Attack"
date: 2026-06-04 21:47:06 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, credential-theft]
severity: critical
must_know: true
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/rust-written-ironworm-npm-supply-chain
---

A Rust-written malware campaign dubbed IronWorm is targeting the npm ecosystem in a
supply chain attack that steals developer credentials and reuses them to propagate
further through the software supply channel. The technique mirrors the TeamPCP
"Shai-Hulud" operation: compromised developer accounts publish trojanized packages that
spread the infection laterally to downstream consumers. Affected developers should
immediately rotate npm access tokens, audit recently published packages for unauthorized
changes, and review their accounts for unexpected publish events.
