---
title: "Critical Flaw Led to Azure Cosmos DB Pwnage"
date: 2026-07-31 09:04:02 +0000
categories: [Daily Signal]
tags: [azure, cloud-security, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/critical-flaw-led-to-azure-cosmos-db-pwnage/
---

A vulnerability named CosmosEscape exposed the primary key for affected Azure
Cosmos DB accounts, granting full read and write access to the database.
Cosmos DB primary keys provide unrestricted account-level control, so
exposure of the key effectively hands over the entire data store.

No detail is available yet on the exploitation vector, patch status, or
whether it was used in the wild. Organizations running Cosmos DB should watch
for Microsoft guidance and consider rotating primary keys as a precaution.
