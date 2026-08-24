---
title: "Critical Keycloak Password Reset Flaw Lets Unauthenticated Attackers Take Over Any Account"
date: 2026-08-24 11:56:34 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, iam, privilege-escalation]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html
---

Red Hat and the Keycloak project released patches for a critical flaw in
the open-source identity and access management server, tracked as
CVE-2026-18963 and rated 9.1 on the CVSS scale.

The bug lets an unauthenticated remote attacker take over any user
account by forcing a password reset — no credentials required.

Organizations running Keycloak should patch immediately; any deployment
using it as a central IAM/SSO provider is a high-value target for account
takeover.
