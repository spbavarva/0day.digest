---
title: "DAEMON Tools Official Installers Backdoored in Supply Chain Attack"
date: 2026-05-05 16:07:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html
---

Kaspersky researchers have identified a supply chain attack against DAEMON Tools, a widely-used virtual drive utility. The malicious installers are distributed directly from the official DAEMON Tools website and signed with legitimate digital certificates belonging to the developers, making them nearly indistinguishable from clean software. Researchers Igor Kuznetsov, Georgy Kucherin, and Leonid Bezvershenko attributed the findings to Kaspersky's GReAT team. Anyone who installed DAEMON Tools recently should treat their system as potentially compromised and verify the integrity of their installation. Organizations with DAEMON Tools in software allowlists should audit recent installs and check for indicators of compromise.
