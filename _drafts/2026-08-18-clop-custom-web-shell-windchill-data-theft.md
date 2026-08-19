---
title: "Clop Created Custom Web Shell for Windchill Data Theft Attacks"
date: 2026-08-18 17:29:51 +0000
categories: [Daily Signal]
tags: [ransomware, malware, data-breach]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/
---

A custom Java web shell likely linked to the Clop ransomware gang was built
specifically to target PTC Windchill and FlexPLM servers. The tool includes
features to decrypt credentials, enumerate file repositories, and exfiltrate
files.

The purpose-built nature of the shell indicates targeted reconnaissance of
these product lifecycle management platforms rather than opportunistic,
off-the-shelf tooling. Organizations running Windchill or FlexPLM should
review server logs for indicators consistent with this activity.
