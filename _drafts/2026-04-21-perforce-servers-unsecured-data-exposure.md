---
title: "1,500+ Perforce P4 Servers Expose Sensitive Data Without Authentication"
date: 2026-04-21 12:37:49 +0000
categories: [Daily Signal]
tags: [data-breach, supply-chain]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/unsecured-perforce-servers-expose-sensitive-data-from-major-orgs/
---

Security researchers have identified over 1,500 Perforce Helix Core (P4) server instances
accessible from the internet that allow unauthenticated read access to files on the server.
Perforce is widely deployed by game studios, defense contractors, financial institutions, and
organizations managing large codebases or binary assets.

Unauthenticated read access to a Perforce server can expose source code, build configurations,
intellectual property, embedded credentials, and API keys stored in build scripts or
configuration files. Source code access enables targeted supply chain attacks, reverse
engineering of proprietary technology, or credential harvesting for downstream systems.

Organizations running Perforce should verify that all P4 instances require authentication for
every connection type, confirm that servers are not directly reachable from untrusted networks,
and scan configuration files and build scripts for embedded credentials that may have been
exposed.
