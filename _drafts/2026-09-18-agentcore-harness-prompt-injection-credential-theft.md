---
title: "Prompt Injection in AWS AgentCore Harness Can Exfiltrate Credentials"
date: 2026-09-18 10:00:36 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, aws, iam]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/
---

Unit 42 researchers found that default configurations in AWS AgentCore
Harness can allow prompt injection attacks to exfiltrate credentials
from AI agent deployments. The research describes a gap between the
harness's execution environment and identity/credential management, and
lays out steps to secure agents built on the platform. Teams running
AgentCore-based agents should review credential handling and harness
configuration defaults.
