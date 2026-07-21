---
title: "New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack"
date: 2026-07-21 07:34:32 +0000
categories: [Daily Signal]
tags: [ransomware, llm, rce, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html
---

Sysdig linked a second attack on the same Langflow server to JADEPUFFER, an
AI-agent-driven threat operator it first documented earlier this month. The
operator has now been observed deploying ENCFORGE, a new compiled Go
ransomware built specifically to encrypt model weights, vector indexes,
training datasets, and other AI infrastructure files across the host
filesystem. The entry point was a Langflow remote code execution flaw.
