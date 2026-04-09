---
title: "Unit 42 Discloses 'Agent God Mode' IAM Escalation in AWS Bedrock AgentCore"
date: 2026-04-08 22:00:51 +0000
categories: [Daily Signal]
tags: [privilege-escalation, cloud-security, llm, aws]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/
---

Unit 42 disclosed an "Agent God Mode" attack against Amazon Bedrock AgentCore
in which overly broad IAM permissions allow an attacker to escalate privileges
and exfiltrate data from the underlying AWS account. The research illustrates
a class of risk specific to AI agent infrastructure where permissive IAM roles
can be abused to gain account-wide control.

AWS Bedrock AgentCore users should audit IAM roles associated with agent
runtimes and enforce least-privilege principles. This finding is part of a
broader trend of AI infrastructure being scrutinized for security
misconfigurations that have no precedent in traditional application security.
