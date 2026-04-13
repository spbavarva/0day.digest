---
title: "Fake Claude Website Distributes PlugX RAT"
date: 2026-04-13 09:52:50 +0000
categories: [Daily Signal]
tags: [malware, anthropic, phishing]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/fake-claude-website-distributes-plugx-rat/
---

Threat actors created a fraudulent website impersonating Anthropic's Claude installer
to distribute PlugX, a remote access trojan historically associated with Chinese APT
groups. The malware abuses DLL sideloading to execute from within a legitimate-looking
application bundle and runs cleanup routines to erase traces of infection post-execution.

The campaign exploits growing public interest in AI tools as a lure. Users who download
Claude or other AI tools from unofficial search results are the primary target. Only
download AI software from verified vendor domains; inspect code signatures and check
hashes before running any installer.
