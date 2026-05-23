---
title: "Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer"
date: 2026-05-23 09:51:13 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, data-breach, php]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
---

Multiple `laravel-lang` packages — including `laravel-lang/lang`, `laravel-lang/http-statuses`, `laravel-lang/attributes`, and `laravel-lang/actions` — have been backdoored to deliver a cross-platform credential-stealing framework. Researchers flagged suspicious timing patterns in newly published tags, indicating a coordinated compromise of the package maintainer pipeline rather than a single account takeover.

Laravel developers should audit installed versions of the affected packages and rotate credentials on any system where a compromised version ran. This is the second Composer-ecosystem supply chain attack reported today, suggesting coordinated or opportunistic targeting of PHP package infrastructure.
