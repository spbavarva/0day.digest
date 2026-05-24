---
title: "Laravel Lang Packages Hijacked to Deploy Credential-Stealing Malware"
date: 2026-05-23 20:48:23 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, github, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/laravel-lang-packages-hijacked-to-deploy-credential-stealing-malware/
---

Attackers compromised the Laravel Lang localization packages and used GitHub
version tag abuse to distribute malicious code through Composer, exposing
developers to a credential-stealing malware campaign. The attack targets the
PHP ecosystem's dependency resolution — when developers run `composer update`,
they may pull the trojanized packages without realizing the upstream source was
tampered with at the tag level rather than the source itself.

Developers using Laravel Lang packages should audit their `composer.lock` for
unexpected version changes, rotate any credentials stored in project
environments, and verify package integrity against known-good hashes. Consider
pinning Composer packages to commit SHAs rather than version tags for
security-sensitive dependencies.
