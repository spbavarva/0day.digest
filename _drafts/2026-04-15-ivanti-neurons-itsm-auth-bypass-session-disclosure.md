---
title: "Ivanti Neurons for ITSM Patches Auth Bypass and Cross-Session Data Disclosure"
date: 2026-04-15 11:38:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/two-vulnerabilities-patched-in-ivanti-neurons-for-itsm/
---

Ivanti has patched two vulnerabilities in Neurons for ITSM: one that allows a remote attacker
to maintain persistent access even after their account has been disabled, and another that
exposes information from other active user sessions.

ITSM platforms are high-value targets because they typically hold broad permissions across IT
infrastructure, including credentials, asset inventories, and change records. An attacker able
to persist after their account is disabled — a condition that should be a hard revocation — can
survive incident response actions and continue operating undetected.

Ivanti has had a difficult run of critical vulnerabilities over the past year. Administrators
should apply the patches, audit active sessions post-patch to confirm no unexpected accounts
remain, and verify that account disablement properly terminates all active tokens.
