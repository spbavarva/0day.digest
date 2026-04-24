---
title: "Bitwarden npm Supply Chain Attack Attributed to TeamPCP; Shai-Hulud Worm Component Identified"
date: 2026-04-24 08:07:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, appsec, devsecops]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/bitwarden-npm-package-hit-in-supply-chain-attack/
---

New attribution details have emerged for the Bitwarden npm supply chain attack reported yesterday:
the campaign has been claimed by a threat actor called TeamPCP and includes a worm component dubbed
Shai-Hulud. The worm element means the malicious payload may propagate beyond the initial
`@bitwarden/cli` compromise to other projects in the same developer environment.

Developers who already rotated credentials following initial disclosure should additionally audit
their environments for Shai-Hulud worm activity in build logs and CI artifact stores. Organizations
with automated pipelines that pulled the compromised package should treat any downstream project
as potentially infected and audit dependencies for secondary payload delivery.
