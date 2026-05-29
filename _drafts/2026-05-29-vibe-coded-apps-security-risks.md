---
title: "2,000 Exposed Vibe-Coded Apps Reveal Shadow AI Risk in Production Environments"
date: 2026-05-29 10:30:00 +0000
categories: [Daily Signal]
tags: [llm, appsec, ai-safety]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html
---

Analysis of more than 2,000 AI-generated "vibe-coded" applications found that employees are routinely building production-grade tools with AI coding assistants, wiring them into internal systems, and publishing them to the internet — without security review or IT involvement.

The report (from Veza's Shadow Builders research) found these apps commonly expose secrets, lack authentication, and connect to sensitive internal data sources. The attack surface has expanded from data pasted into ChatGPT to fully deployed applications with live API connections.

Enterprises should extend AppSec and SAST scanning to cover AI-generated code, and add discovery tooling for unauthorized externally-facing applications. Security awareness programs need to explicitly address the risks of AI-assisted app development reaching production.
