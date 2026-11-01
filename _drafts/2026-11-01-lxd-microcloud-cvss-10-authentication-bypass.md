---
title: "CVSS 10.0 Flaw in Canonical LXD, MicroCloud Lets Attackers Impersonate Trusted Clients"
date: 2026-11-01 08:51:31 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation, container-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html
---

A critical authentication bypass in Canonical's LXD and MicroCloud, rated
CVSS 10.0, lets an attacker log in as a trusted client without holding
that client's private key.

Exploitation requires network access to the target's HTTPS API plus the
trusted client's public certificate -- no private key needed.

Once authenticated as the impersonated client, an attacker gains access to
the cluster and its virtual machines, with impact scaling to whatever
privileges that client held.
