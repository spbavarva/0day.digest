---
title: "Kimsuky Deploys HTTPSpy and HelloDoor Malware, Abuses VS Code Tunnels for C2"
date: 2026-05-29 05:57:41 +0000
categories: [Daily Signal]
tags: [malware, phishing, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html
---

North Korean APT Kimsuky (Velvet Chollima) ran a campaign against South Korean military and corporate targets through March–April 2026 deploying two new tools: HTTPSpy for credential interception and HelloDoor as a backdoor. The group also tunneled C2 traffic through Visual Studio Code's remote tunneling feature — a legitimate Microsoft service — making traffic harder to detect on standard network controls.

The VS Code tunnel abuse is a notable TTPs expansion: attackers are embedding C2 in legitimate developer tooling already whitelisted in many environments. The lure techniques included spoofed security software installers and a fake Webex meeting page.

Security teams should monitor VS Code tunnel usage via endpoint telemetry, particularly on non-developer machines. Any organization with South Korea or DPRK threat exposure should treat unsolicited Webex meeting invites and security software prompts as high-priority social engineering indicators.
