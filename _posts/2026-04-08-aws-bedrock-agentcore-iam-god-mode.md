---
title: "AWS Bedrock AgentCore Flaw Enables \"Agent God Mode\" via IAM Privilege Escalation"
date: 2026-04-08 22:00:51 +0000
categories: [Daily Signal]
tags: [privilege-escalation, cloud-security, aws, llm]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/
---

Unit 42 researchers found that Amazon Bedrock AgentCore assigns AI agents overly broad IAM permissions by default, enabling privilege escalation to near-full AWS account control — what researchers dubbed "Agent God Mode." A successful exploit allows unrestricted data exfiltration across the account.

This is a significant finding as agentic AI deployment in cloud environments grows. Organizations using Bedrock AgentCore should immediately audit IAM roles attached to their agents, apply least-privilege policies, and review what data each agent can access. The blast radius of a compromised AI agent can equal that of a compromised root credential.
