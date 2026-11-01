---
title: "CVSS 10.0 LXD/MicroCloud Flaw Lets Attackers Impersonate Trusted Clients"
date: 2026-11-01 08:51:31 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, container-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html
---

A CVSS 10.0 flaw in Canonical's LXD and MicroCloud lets an attacker
impersonate a trusted client on the clustering HTTPS API without ever
holding that client's private key. The attacker only needs network
access to the API and the impersonated client's public certificate.

Once impersonated, the attacker inherits that client's access to the
cluster and its virtual machines — for privileged clients, this can mean
full cluster control. Operators running LXD or MicroCloud clusters
should check Canonical's advisories for a fix.
