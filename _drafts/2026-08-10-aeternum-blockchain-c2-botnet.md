---
title: "The Permanent Threat: Analyzing Aeternum's Blockchain-Based C2 Operations and Communications"
date: 2026-08-10 22:00:02 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/
---

Unit 42 analyzed the Aeternum botnet loader, which uses Polygon blockchain
smart contracts as decentralized command-and-control infrastructure for
payload delivery and communication.

Routing C2 through a blockchain removes the single points of failure that
let defenders take down traditional centralized C2 servers, making the
infrastructure harder to disrupt.
