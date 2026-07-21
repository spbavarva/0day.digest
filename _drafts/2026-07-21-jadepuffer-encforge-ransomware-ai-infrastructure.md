---
title: "JadePuffer Deploys ENCFORGE Ransomware Against AI Infrastructure"
date: 2026-07-21 07:34:32 +0000
categories: [Daily Signal]
tags: [ransomware, malware, rce, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html
---

Sysdig researchers linked a second attack against a Langflow server to
JADEPUFFER, an AI-agent-driven threat actor. The operator is now deploying
ENCFORGE, a new compiled-Go ransomware built specifically to encrypt AI
infrastructure files — model weights, vector indexes, and training
datasets — rather than general-purpose file types. The campaign begins with
remote code execution against exposed Langflow servers. Organizations
running Langflow or similar AI orchestration tools should ensure instances
aren't exposed to the internet and are fully patched.
