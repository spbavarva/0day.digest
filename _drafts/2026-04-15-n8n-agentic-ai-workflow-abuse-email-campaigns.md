---
title: "Threat Actors Abusing n8n Agentic AI Workflow Platform in Email Attack Campaigns"
date: 2026-04-15 10:00:00 +0000
categories: [Daily Signal]
tags: [malware, phishing, llm]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/the-n8n-n8mare/
---

Cisco Talos has documented threat actors abusing n8n, an open-source agentic AI workflow
automation platform, in malicious email campaigns running from at least October 2025 through
March 2026. n8n allows chaining AI model calls, webhooks, and external services into automated
pipelines — capabilities attackers are exploiting to orchestrate phishing and delivery workflows.

The research highlights a growing pattern of AI workflow tooling being co-opted for offensive
operations. Because n8n supports self-hosting and has legitimate enterprise use cases, network
defenders cannot simply block the platform at the perimeter without operational impact.

Security teams should review internal n8n deployments for unauthorized webhook integrations,
monitor outbound traffic to n8n cloud instances from unexpected hosts, and treat AI automation
platforms with the same scrutiny as RMM tools. Talos's full write-up includes indicators of
compromise.
