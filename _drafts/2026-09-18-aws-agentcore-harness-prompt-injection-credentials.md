---
title: "Default AWS AgentCore Harness Configs Allow Prompt Injection to Exfiltrate Credentials"
date: 2026-09-18 10:00:36 +0000
categories: [Daily Signal]
tags: [llm, aws, iam, ai-safety, cloud-security]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto Networks)
    url: https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/
---

Unit 42 analyzed how default configurations in AWS AgentCore Harness
create space between the agent's execution environment and its identity
boundary, allowing prompt injection to exfiltrate credentials. The
researchers outline concrete hardening steps for teams running agents on
AgentCore.
