---
title: "Malicious npm Package Exfiltrated Files from Claude AI User Directories"
date: 2026-05-27 15:44:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware, anthropic, llm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html
---

OX Security researchers found a malicious npm package named
"mouse5212-super-formatter" that uploads files from "/mnt/user-data", the
directory Anthropic's Claude AI tool uses for uploads and session outputs.

The package is a targeted infostealer aimed at developers who run Claude Code
or Claude-based tooling locally. Any developer who installed this package should
treat their Claude user data directory as compromised. Audit npm dependency trees
for unrecognized packages and review file access logs for unexpected outbound
transfers.
