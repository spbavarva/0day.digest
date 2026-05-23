---
title: "China's Webworm APT Abuses Discord and Microsoft Graph to Compromise EU Governments"
date: 2026-05-22 07:01:00 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, microsoft]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
---

Chinese APT group Webworm is targeting EU government networks by routing command-and-control traffic through Discord and the Microsoft Graph API, blending malicious activity with legitimate cloud service communications. The group also employs SoftEther VPN SOCKS proxies for tunneling between compromised hosts and attacker infrastructure. Network controls that block known malicious IPs provide little protection when C2 runs over Microsoft or Discord endpoints. Defenders should monitor for anomalous Graph API call patterns and unexpected SoftEther VPN processes on government workstations.
