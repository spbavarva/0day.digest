---
title: "Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across ~100 Repositories"
date: 2026-09-16 13:37:07 +0000
categories: [Daily Signal]
tags: [supply-chain, llm, malware, github]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html
---

Mandiant reported that an attacker hijacked an active AI coding-assistant
session at an unnamed SaaS provider and used it to spread the Shai-Hulud
worm across roughly 100 internal code repositories. Before the worm
spread, the compromised assistant recommended attacker-poisoned software,
which was accepted and executed.

The worm then stole repository secrets and source code across the
affected repos — a concrete example of an AI coding assistant being
weaponized as a supply-chain attack vector.
