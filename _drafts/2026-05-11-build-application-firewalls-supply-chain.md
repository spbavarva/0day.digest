---
title: "Build Application Firewalls: Runtime Inspection as a New Supply Chain Defense Layer"
date: 2026-05-11 14:06:01 +0000
categories: [Daily Signal]
tags: [supply-chain, devsecops, appsec]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/build-application-firewalls-aim-to-stop-the-next-supply-chain-attack/
---

A new defensive category called Build Application Firewalls (BAFs) is emerging to address
supply chain attacks at the CI/CD build stage. Unlike static analysis or SCA tools that
scan dependency manifests, BAFs monitor what a build process actually executes at runtime —
network connections, file writes, subprocess calls — to catch malicious behavior from
poisoned packages or compromised build tools.

Several vendors are entering this space as a response to high-profile CI/CD poisoning
incidents where malicious code in dependencies only triggered during the build phase.
Organizations running self-hosted or cloud CI pipelines should evaluate whether they have
any runtime-level visibility into build behavior, or whether their current tooling would
have caught the Checkmarx Jenkins plugin compromise disclosed today.
