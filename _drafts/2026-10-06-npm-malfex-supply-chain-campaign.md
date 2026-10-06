---
title: "Long-Running MALFEX npm Supply Chain Campaign Accumulates 40,000 Downloads"
date: 2026-10-06 10:34:25 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/long-running-npm-malware-campaign-accumulates-40000-downloads/
---

A supply chain campaign tracked as MALFEX has published eight malicious npm
packages since August 2023, accumulating roughly 40,000 downloads over its
lifetime. The long operating window — more than two years — suggests the
packages evaded detection by npm's registry defenses and typical dependency
scanning for an extended period. Specific payload behavior and targeting
were not detailed in the report covered. Teams should audit dependency trees
for the identified MALFEX packages and rotate any credentials potentially
exposed via affected builds.
