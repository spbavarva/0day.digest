---
title: "Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug"
date: 2026-08-05 14:27:30 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, cloud-security, privilege-escalation]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
---

HashiCorp, Veeam, and the Django Software Foundation have patched 11
vulnerabilities across Terraform MCP Server, Veeam Service Provider
Console, and Django.

The two most serious: an unauthenticated flaw in Veeam's console that hands
over a managed agent's credentials (rated 9.5), and a cross-tenant flaw in
HashiCorp's Terraform MCP server that lets one user's Terraform token be
reused for a later user's session (CVSS 10.0). Organizations running any of
these should patch immediately given the cross-tenant token exposure.
</content>
