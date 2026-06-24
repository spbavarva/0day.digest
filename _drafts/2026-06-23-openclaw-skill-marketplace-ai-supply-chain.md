---
title: "OpenClaw's Skill Marketplace and the Emerging AI Supply Chain Threat"
date: 2026-06-23 22:00:51 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, llm, ai-safety]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/
---

Unit 42 analyzed ClawHub, the skill marketplace for the OpenClaw AI
agent platform, and found evasive malicious skills that bypass the
marketplace's automated security scanners. According to the research,
these skills have been used to deploy infostealer malware and to
execute agentic financial fraud. The findings point to an emerging AI
supply chain risk as agent platforms adopt plugin/skill marketplaces
with trust and vetting gaps similar to npm or PyPI. Teams using AI agent
marketplaces should treat third-party skills as untrusted code until
vetted.
