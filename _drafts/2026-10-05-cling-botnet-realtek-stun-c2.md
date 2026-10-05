---
title: "Realtek Jungle SDK Exploit Attempts Deliver Cling Botnet With STUN-Based C2"
date: 2026-10-05 11:46:25 +0000
categories: [Daily Signal]
tags: [malware, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/realtek-jungle-sdk-exploit-attempts.html
  - name: Dark Reading
    url: https://www.darkreading.com/iot/clingstun-vulnerable-iot-devices-proxy-nodes
---

Threat actors are attempting to exploit a now-patched critical flaw in the
Realtek Jungle SDK to deploy a botnet malware called Cling. Per a Nozomi
Networks report, Cling repurposes ordinary STUN protocol behavior into a
practical command-and-control channel rather than introducing a new
propagation technique.

A related Linux backdoor, tracked as ClingSTUN, reportedly exploits around
two dozen known flaws to compromise IoT devices and uses legitimate public
STUN servers to obscure its communications, turning infected devices into
proxy nodes.
