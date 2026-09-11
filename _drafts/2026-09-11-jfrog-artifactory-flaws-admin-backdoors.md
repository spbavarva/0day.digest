---
title: "Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors"
date: 2026-09-11 07:31:05 +0000
categories: [Daily Signal]
tags: [supply-chain, rce, privilege-escalation, wiz]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html
---

Attackers chained two vulnerabilities in JFrog Artifactory, the repository
software build pipelines pull dependencies from, to gain administrator
control of self-hosted servers and plant backdoors. Wiz observed the attacks
between August 15 and September 8; JFrog had already fixed both flaws before
the campaign, so only unpatched self-hosted servers were exposed. Because
Artifactory sits directly in build and release pipelines, admin-level
compromise creates supply chain risk for anyone consuming artifacts it
serves. Self-hosted Artifactory operators should confirm they're on a
patched version and audit for unauthorized admin accounts or backdoors.
