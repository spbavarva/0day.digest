---
title: "SAP npm Packages Compromised in Credential-Stealing Supply Chain Attack"
date: 2026-04-29 16:26:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html
---

Researchers from Aikido Security, SafeDep, Socket, StepSecurity, and Wiz identified a coordinated supply chain campaign dubbed "mini Shai-Hulud" that compromised multiple SAP-related npm packages with credential-stealing malware. The campaign targets JavaScript and cloud application developers who depend on these packages within SAP ecosystems, modifying them to exfiltrate developer credentials and environment variables.

Organizations using SAP JavaScript SDKs should audit their npm dependency trees immediately and rotate any credentials exposed in affected environments. This follows a pattern of attackers targeting enterprise software ecosystems where trust in vendor-adjacent packages is elevated. Five independent security firms corroborating the same campaign suggests broad impact.
