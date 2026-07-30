---
title: "Azure Cosmos DB Flaw 'CosmosEscape' Exposed Platform-Wide Key"
date: 2026-07-30 13:34:09 +0000
categories: [Daily Signal]
tags: [cloud-security, azure, vulnerability, wiz]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html
---

Wiz disclosed a now-patched vulnerability in Azure Cosmos DB that could have
let an attacker escape the service's Gremlin query sandbox and gain full
read/write access to databases across customer tenants.

The exploit chain, codenamed CosmosEscape, reportedly began with a crafted
query against an attacker-controlled Gremlin database and led to code
execution. Microsoft has patched the issue; no customer exploitation has
been reported.
