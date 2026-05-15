---
title: "TeamPCP Releases Shai-Hulud Worm Source Code, Invites Supply Chain Attacks with Monetary Rewards"
date: 2026-05-15 09:47:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, npm]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/teampcp-ups-the-game-releases-shai-hulud-worms-source-code/
---

TeamPCP, the threat actor behind the Shai-Hulud supply chain worm already used against Bitwarden, TanStack, and OpenAI's corporate environment, publicly released the worm's full source code. The group is actively recruiting other threat actors to deploy it in new supply chain attacks and offering monetary rewards for successful compromises. Open-sourcing this tooling dramatically lowers the barrier for copycat campaigns targeting npm and potentially other package ecosystems. Security teams should increase scrutiny of newly published and recently updated packages, enforce lock-file pinning in CI/CD pipelines, and verify package checksums against trusted registries before deployment.
