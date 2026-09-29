---
title: "Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials"
date: 2026-09-29 06:08:25 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, supply-chain]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html
---

A flaw in the official MCP Python SDK could let a malicious MCP server trick
a connecting application into handing over the OAuth credentials it uses to
authenticate to a real service.

Affected versions sent the client secret, authorization code, and PKCE proof
key to a token endpoint controlled by the attacker-run server. The issue is
fixed in SDK version 1.30.0; applications built on the MCP Python SDK should
upgrade.
