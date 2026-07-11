---
title: "'Ghostcommit' Hides Prompt Injection in Images to Fool AI Agents, Steal Secrets"
date: 2026-07-11 09:03:57 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, supply-chain, github]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/
---

Researchers demonstrated a technique dubbed "Ghostcommit" that hides prompt injection payloads inside PNG images to manipulate AI coding agents. The hidden instructions slipped past AI code reviewers CodeRabbit and Bugbot, which don't open image files at all, then convinced a coding agent to read a repository's .env file and write its secrets into code as a list of numbers. The technique exposes a blind spot in AI-assisted code review: image content isn't currently vetted for embedded instructions. Teams running AI coding agents or review bots on repos with image assets should treat image content as untrusted input.
