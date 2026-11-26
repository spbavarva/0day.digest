---
title: "Secure Agentic Access to AWS with Enterprise-Managed Authorization"
date: 2026-11-25 21:00:37 +0000
categories: [Daily Signal]
tags: [aws, cloud-security, iam]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/secure-agentic-access-to-aws-with-enterprise-managed-authorization/
---

AWS Sign-In now supports Enterprise-Managed Authorization (EMA) using the
Identity Assertion JWT Authorization Grant (ID-JAG). The feature lets
organizations securely authorize AI agents to access the AWS MCP Server.

Authorization is managed through existing enterprise identity providers,
such as Okta, rather than separate credentials per agent.

This gives organizations centralized control over which applications and
agents can reach AWS resources, relevant to teams deploying AI agents
against production AWS environments.
