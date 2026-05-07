---
title: "TeamPCP 'Mini Shai-Hulud' Supply Chain Attack Hits SAP npm Packages"
date: 2026-05-01 07:33:40 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/1800-hit-in-mini-shai-hulud-attack-on-sap-lightning-intercom/
---

The TeamPCP threat group has compromised multiple npm packages used in SAP's cloud application development ecosystem—including the Lightning and Intercom packages—in a campaign dubbed "Mini Shai-Hulud." The two compromised packages together have nearly 10 million combined monthly downloads.

SecurityWeek reports 1,800 systems were directly hit in this attack wave. SAP developers should audit their npm dependency trees, check installed versions of Lightning and Intercom for unauthorized modifications, and update to clean, verified releases immediately.

This follows a pattern of supply chain campaigns broadening to enterprise developer tooling. TeamPCP's targeting of SAP ecosystem packages suggests deliberate focus on high-value corporate environments where these packages are commonly deployed.
