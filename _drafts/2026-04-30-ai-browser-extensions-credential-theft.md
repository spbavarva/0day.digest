---
title: "High-Risk AI Browser Extensions Intercepting Prompts and Stealing Passwords"
date: 2026-04-30 22:00:57 +0000
categories: [Daily Signal]
tags: [malware, llm, appsec, phishing]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/
---

Unit 42 has identified a class of malicious generative AI browser extensions that operate far beyond their advertised functionality. Disguised as email writing assistants and productivity tools, they intercept user prompts sent to AI services, steal passwords captured in form inputs, and exfiltrate session data to attacker-controlled infrastructure.

The extensions exploit users' trust in AI tooling and the expectation that AI interactions are private. They target both consumer credentials and enterprise sessions, making them a meaningful lateral movement risk in corporate environments.

Organizations should immediately audit browser extensions installed by employees, enforce an allowlist-only policy for enterprise browsers, and flag any extension claiming AI functionality that requests broad host permissions. The Unit 42 post includes indicators and extension identifiers.
