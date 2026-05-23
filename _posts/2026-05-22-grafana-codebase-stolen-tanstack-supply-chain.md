---
title: "Grafana Codebase Stolen via TanStack Supply Chain Attack"
date: 2026-05-22 07:49:38 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/grafana-says-codebase-and-other-data-stolen-via-tanstack-supply-chain-attack/
---

Attackers accessed Grafana's GitHub repositories using a token that was compromised in the earlier TanStack supply chain attack but never rotated after that incident. Grafana confirmed its codebase and other data were exfiltrated. The failure to rotate a known-exposed token is the direct root cause. Organizations that may have been affected by the TanStack compromise should audit all tokens and credentials for rotation status — an unrotated token from a prior supply chain incident is an open door.
