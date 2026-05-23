---
title: "Packagist Supply Chain Attack Injects Linux Malware Into 8 Composer Packages"
date: 2026-05-23 16:07:51 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, github, php]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/packagist-supply-chain-attack-infects-8.html
---

Eight Packagist (Composer) packages have been compromised in a coordinated supply chain attack. The malicious code was inserted into `package.json` rather than `composer.json`, causing it to target projects that ship both PHP and JavaScript. The payload downloads and executes a Linux binary hosted on GitHub Releases.

The `package.json` injection point is a deliberate evasion: security scanners focused on Composer dependency trees would miss it entirely. Audit recent installs of affected packages, check for unexpected outbound connections to GitHub Releases CDN, and pin Composer package versions where possible.
