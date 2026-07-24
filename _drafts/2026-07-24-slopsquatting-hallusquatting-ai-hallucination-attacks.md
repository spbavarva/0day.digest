---
title: "Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack"
date: 2026-07-24 14:01:11 +0000
categories: [Daily Signal]
tags: [supply-chain, ai-safety, llm, npm, pypi]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
---

Slopsquatting, phantom-domain squatting, and HalluSquatting all exploit
the same late-binding attack pattern: AI coding agents trust package,
repo, or domain names that the model hallucinated rather than ones that
actually exist. Attackers register those hallucinated names in advance so
that when an agent later "trusts" them, it pulls malicious code or content
into a build pipeline. ActiveState says pre-fetch verification and
governed dependency management can stop the attack before it reaches
production.
