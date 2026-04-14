---
title: "Fake Claude Website Delivers PlugX RAT via DLL Sideloading"
date: 2026-04-13 09:52:50 +0000
categories: [Daily Signal]
tags: [malware, anthropic, phishing]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/fake-claude-website-distributes-plugx-rat/
---

Threat actors have created a fraudulent Anthropic/Claude installation website that delivers
the PlugX remote access trojan. The installer mimics a legitimate Anthropic package and uses
DLL sideloading to deploy PlugX while removing forensic artifacts to hinder detection.

PlugX is a well-established China-linked RAT with capabilities for persistent access, lateral
movement, keylogging, and data exfiltration. The campaign exploits broad public interest in
AI tools to social-engineer users into running a malicious installer. Users should download
Claude only from official Anthropic channels (anthropic.com or claude.ai), verify package
signatures where available, and treat any unsolicited link or social media post promoting
a Claude download with immediate suspicion.
