---
title: "Microsoft GitHub Repos Compromised to Push Password-Stealing Malware (Miasma)"
date: 2026-06-09 15:42:40 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, github, microsoft, data-breach]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/github-disables-microsoft-repos-pushing-password-stealing-malware/
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/microsoft-restores-some-github-repos.html
---

Microsoft removed 73 repositories across its Azure, microsoft, Azure-Samples, and MicrosoftDocs GitHub organizations after attackers injected an information stealer into open-source project code.
The incident, part of an ongoing probe dubbed Miasma, disrupted continuous integration pipelines for downstream consumers of the compromised repos.
Microsoft confirmed it is restoring some repositories while keeping others offline as the investigation continues.
Any developer or organization consuming packages or workflows from the affected Microsoft GitHub orgs in the past several days should audit their dependency graphs and build artifacts for the infostealer payload.
This is a supply-chain compromise of a major OSS maintainer — downstream impact may be broad.
