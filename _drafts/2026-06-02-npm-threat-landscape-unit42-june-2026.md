---
title: "Unit 42 Updates npm Threat Landscape: Wormable Malware, CI/CD Persistence, Multi-Stage Attacks"
date: 2026-06-02 17:30:00 +0000
categories: [Daily Signal]
tags: [npm, supply-chain, malware, devsecops]
severity: medium
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
---

Unit 42 has released an updated analysis of the npm supply chain threat landscape following the post-Shai Hulud wave of attacks. Key findings include wormable malware that spreads laterally through CI/CD pipelines, multi-stage attack chains that blend into legitimate build tooling, and persistence mechanisms designed to survive package removal or quarantine. The update was published the same day as the Red Hat npm supply chain incident affecting 32 packages and ~117k weekly downloads. Development teams should audit npm dependency chains, restrict publish token permissions, and deploy runtime monitoring in CI/CD environments.
