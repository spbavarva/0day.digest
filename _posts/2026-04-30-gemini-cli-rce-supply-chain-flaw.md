---
title: "Critical Gemini CLI Flaw Enabled Host Code Execution and Supply Chain Attacks"
date: 2026-04-30 12:34:05 +0000
categories: [Daily Signal]
tags: [rce, supply-chain, google, vulnerability]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/critical-gemini-cli-flaw-enabled-host-code-execution-supply-chain-attacks/
---

A critical vulnerability in Google's Gemini CLI allowed an attacker to plant a malicious configuration file that executed arbitrary commands outside the tool's sandboxed environment. The flaw created a supply chain attack vector: a poisoned config committed to a shared repository could silently execute code on any developer machine running the CLI against that project. The vulnerability has been patched by Google.

Developers using Gemini CLI should update to the latest version immediately. Audit any third-party or shared configuration files included in projects that use the CLI, and treat unexpected config changes as an indicator of compromise.
