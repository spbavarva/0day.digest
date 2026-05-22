---
title: "China's Webworm APT Abuses Discord and Microsoft Graph API to Target EU Governments"
date: 2026-05-22 07:01:00 +0000
categories: [Daily Signal]
tags: [apt, cloud-security, microsoft, malware]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
---

Chinese advanced persistent threat group Webworm is using Discord and the Microsoft Graph API as
command-and-control channels in intrusions against European government targets. The group also relies
on SoftEther VPN-based SOCKS proxies to tunnel traffic between victims and attacker infrastructure,
blending into legitimate cloud service traffic.

Abusing trusted platforms like Discord and Microsoft 365 makes Webworm's traffic difficult to
distinguish from normal enterprise communications. Defenders should review cloud service egress
policies and monitor for unusual Graph API calls or Discord connections from endpoints that have no
business need to reach those services.
