---
title: "OVHcloud CLI Releases Hijacked on GitHub to Steal Developer Secrets"
date: 2026-10-20 11:31:22 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, github]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ovhcloud-cli-releases-backdoored-on-github-to-steal-developer-secrets/
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/hackers-hijack-five-ovhcloud-cli.html
---

An attacker used a hijacked contributor GitHub account to replace the
download archives on five existing OVHcloud CLI releases on October 19,
swapping in a build designed to steal secrets stored on disk. The malicious
files were live on GitHub for up to 94 minutes, from 12:47 to 14:21 UTC.

OVHcloud is warning developers who downloaded the CLI during that window to
treat local secrets as compromised and rotate them.
