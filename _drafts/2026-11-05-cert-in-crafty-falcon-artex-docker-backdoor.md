---
title: "CERT-In Flags AI-Driven Threat Actor Exploiting Backdoored ARTEX Docker Image"
date: 2026-11-05 08:42:03 +0000
categories: [Daily Signal]
tags: [supply-chain, container-security, malware, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html
---

India's CERT-In disclosed that an AI-assisted threat actor it tracks as
Crafty Falcon is targeting Banking, Financial Services, and Insurance (BFSI)
organizations in India using publicly available AI-driven offensive
security tools. The activity involves a backdoored Docker image for ARTEX
that exposed 62 management consoles to root access.

CERT-In describes the activity as active and ongoing. BFSI organizations in
India running ARTEX should check their Docker images against known-good
sources and audit exposed management consoles for unauthorized root access.
