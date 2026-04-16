---
title: "Prompt Injection Flaws in Salesforce Agentforce and Microsoft Copilot Now Patched"
date: 2026-04-15 12:00:00 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws
---

Security researchers discovered prompt injection vulnerabilities in Salesforce Agentforce and
Microsoft Copilot that would have allowed external attackers to exfiltrate sensitive data
processed by the AI agents. Both vendors have released patches addressing the issues.

Prompt injection is one of the most pervasive attack classes in deployed AI systems. When AI
agents process untrusted external content—emails, documents, web pages—malicious instructions
embedded in that content can redirect the agent to perform unauthorized actions or leak data
already in its context window. These two disclosures follow a pattern of enterprise AI platforms
shipping with insufficient trust boundaries around external input.

Organizations should ensure they are running patched versions of both platforms. Security teams
should treat prompt injection as a first-class threat in AI agent threat models and establish
red-teaming processes for agents with access to sensitive data.
