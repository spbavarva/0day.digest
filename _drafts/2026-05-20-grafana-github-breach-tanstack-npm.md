---
title: "Grafana Labs Source Code Exposed via GitHub Breach Linked to TanStack npm Attack"
date: 2026-05-20 05:12:06 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach, grafana, npm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html
---

Grafana Labs confirmed on May 19, 2026 that its GitHub environment was breached, exposing public and
private source code along with internal repositories. The incident is linked to a TanStack npm
package attack. The company found no evidence of customer production systems or operations being
compromised.

The breach appears to be part of a broader wave of GitHub-targeted supply chain attacks, coinciding
with the TeamPCP campaign that also compromised GitHub's own internal repositories. Organizations
using Grafana or depending on its open-source tooling should monitor for unexpected behavior or
tampered releases until Grafana provides a clean bill of health on affected code.
