---
title: "Amazon Q VS Code Extension Flaw Enables Cloud Credential Theft"
date: 2026-06-29 11:44:42 +0000
categories: [Daily Signal]
tags: [vulnerability, aws, cloud-security]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cloud-security/amazon-q-vs-extension-flaw-leads-cloud-credential-theft
---

A vulnerability in the Amazon Q Visual Studio Code extension lets an
attacker plant a malicious repository that executes arbitrary code and
steals cloud credentials when opened by a victim using the extension.

The flaw highlights growing risk around Model Context Protocol (MCP)
integrations in AI coding tools, where untrusted repository content can
reach privileged local execution paths. Developers using the Amazon Q VS
Code extension should update to the patched version.
