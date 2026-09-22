---
title: "Shai-Hulud Supply Chain Attack Hits CrowdSec's GitHub Data via TanStack npm Compromise"
date: 2026-09-22 17:32:49 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, github, data-breach]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/shai-hulud-attack-cyber-firm-crowdsec-github-data
---

Threat actors stole 170 private GitHub repositories belonging to
cybersecurity firm CrowdSec using an OAuth token taken from a former
employee's computer.

The token was obtained through the TanStack npm supply chain attack, part
of the broader Shai-Hulud campaign. Organizations should audit and revoke
OAuth tokens tied to former employees, especially those with GitHub scopes.
