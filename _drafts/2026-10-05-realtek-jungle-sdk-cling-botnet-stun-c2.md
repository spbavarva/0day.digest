---
title: "Realtek Jungle SDK Exploits Deliver Cling Botnet Over STUN-Based C2"
date: 2026-10-05 11:46:25 +0000
categories: [Daily Signal]
tags: [malware, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/realtek-jungle-sdk-exploit-attempts.html
---

Threat actors are attempting to exploit a now-patched critical flaw in
the Realtek Jungle SDK to deploy botnet malware called Cling. Nozomi
Networks reports Cling is notable not for a new propagation technique,
but for repurposing ordinary STUN protocol behavior into a practical
command-and-control channel. Devices running unpatched Realtek Jungle
SDK firmware remain at risk. Vendors and integrators using this SDK
should confirm they're on a patched version.
