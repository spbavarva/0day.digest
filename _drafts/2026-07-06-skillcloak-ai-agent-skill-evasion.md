---
title: "SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners"
date: 2026-07-06 06:33:56 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, supply-chain]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html
---

Researchers at the Hong Kong University of Science and Technology showed
that scanners meant to catch malicious "skill" add-ons for AI coding agents
can be defeated with simple self-extracting packing tricks. The strongest
packing technique evaded every scanner tested more than 90% of the time
while leaving the malicious skill fully functional. The same team built a
runtime checker that catches most of the packed variants, suggesting static
scanning alone isn't sufficient for AI agent skill marketplaces. This is a
supply-chain-style risk for any workflow that installs third-party skills
into AI coding agents.
