---
title: "SonicWall Patches CVSS 10.0 Pre-Authentication SSRF Flaw in SMA1000 Appliances"
date: 2026-10-07 16:17:44 +0000
categories: [Daily Signal]
tags: [ssrf, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/sonicwall-patches-cvss-100-pre.html
---

SonicWall has released hotfixes for four vulnerabilities in its SMA1000 series
secure access gateways, appliances that give remote workers access to
internal company networks and applications.

The most severe issue is a pre-authentication server-side request forgery
flaw rated CVSS 10.0, the maximum possible score. An attacker with no valid
credentials can send crafted requests through the appliance to reach internal
functions.

SonicWall says it has no evidence of exploitation of any of the four flaws
so far. Administrators running SMA1000 appliances should apply the hotfixes
immediately given the appliance's internet-facing role.
</content>
