---
title: "ChainDrop: Inside a Self-Propagating npm Worm"
date: 2026-08-06 22:26:39 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/
---

Unit 42 detailed ChainDrop, a self-propagating worm spreading through the npm
registry. The worm extracts secrets from GitHub Actions runners and uses
Ethereum smart contracts for command-and-control routing, an unusual choice
that complicates takedown. Self-propagation lets it spread automatically
between compromised packages and maintainer accounts without further attacker
action. Teams should audit CI/CD secrets exposure and review recently
published or updated npm dependencies for unexpected postinstall behavior.
