---
title: "Shai-Hulud / Hades Supply Chain Campaign Hits 100+ npm and PyPI Packages"
date: 2026-06-09 11:37:11 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, npm, malware, data-breach]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/over-100-npm-pypi-packages-hit-in-new-shai-hulud-supply-chain-attacks/
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html
---

The ongoing Shai-Hulud supply chain campaign has spawned two new attack waves — Miasma (targeting GitHub/npm) and Hades (targeting PyPI) — compromising over 100 packages across both ecosystems.
The Hades variant placed 37 malicious wheel artifacts across 19 PyPI packages; each shipped a `*-setup.pth` file that executes automatically on Python environment startup to run a Bun-based credential stealer.
The self-propagating attack design is being actively refined and specialized to target individual ecosystems separately.
Developers should audit installed packages for unexpected `.pth` files and verify package integrity against published checksums; remove any packages released by the affected maintainers since the campaign began.
