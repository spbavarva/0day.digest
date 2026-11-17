---
title: "OPTIMJACK Supply Chain Attack Injects Malware via Optimizely Platform on 178 Major Sites"
date: 2026-11-17 20:43:14 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach]
severity: critical
must_know: true
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/optimjack-supply-chain-attack/
  - name: SecurityWeek
    url: https://www.securityweek.com/optimizely-vulnerability-exploited-to-serve-malware-on-major-websites/
---

A supply chain attack dubbed OPTIMJACK compromised a vendor script used by
the Optimizely website-experimentation platform, letting attackers inject
malicious JavaScript into customer sites. Researchers identified malicious
code on 178 widely visited websites, and Optimizely has confirmed the
breach. Affected organizations reportedly include BBC, CNN, Zoom, GitLab,
Salesforce, Equifax, HSBC, and IKEA, exposing their site visitors to the
injected malware.

Unit 42 says the incident underscores the risk of relying on third-party
vendor scripts without strict segmentation. Organizations using Optimizely
should audit for the injected script and review segmentation controls for
third-party JavaScript on production sites.
