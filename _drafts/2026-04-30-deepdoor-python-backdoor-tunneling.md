---
title: "DEEP#DOOR Python Backdoor Uses Tunneling Services to Steal Browser and Cloud Credentials"
date: 2026-04-30 12:36:00 +0000
categories: [Daily Signal]
tags: [malware, phishing, credential-theft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/new-python-backdoor-uses-tunneling.html
---

Researchers disclosed DEEP#DOOR, a stealthy Python-based backdoor framework that establishes persistent access on Windows hosts and harvests browser credentials, cloud tokens, and sensitive system information. The infection chain begins with a batch script (`install_obf.bat`) that disables Windows security controls before deploying the Python payload — suggesting delivery via trojanized installers or phishing.

The framework routes C2 traffic through a tunneling service, making egress detection harder at the perimeter. Hunt for: unsigned batch scripts disabling Defender, unexpected Python interpreter invocations, and tunneling tool processes (e.g., Cloudflare Tunnel, ngrok) spawned from non-standard parent processes. Any cloud credentials present on infected hosts should be treated as compromised and rotated.
