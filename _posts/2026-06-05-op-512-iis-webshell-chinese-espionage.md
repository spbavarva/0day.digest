---
title: "New Chinese Espionage Cluster OP-512 Targets IIS Servers With Custom Web Shell Framework"
date: 2026-06-05 12:33:38 +0000
categories: [Daily Signal]
tags: [malware, microsoft, vulnerability, apt]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-threat-cluster-op-512-targets.html
---

Researchers at ReliaQuest have uncovered a previously unreported threat cluster, OP-512, assessed with
moderate-to-high confidence to be China-linked and espionage-focused. The group deploys a bespoke web
shell framework against Microsoft IIS servers to establish persistent footholds. Custom web shell
frameworks are characteristic of sophisticated nation-state actors who prioritize long-term access over
noisy exploitation. Organizations running IIS should audit web-accessible directories for unexpected
script files, review IIS module configurations, and ensure web application firewall rules are current.
Hunting for OP-512 IOCs in HTTP logs and file system artifacts is recommended.
