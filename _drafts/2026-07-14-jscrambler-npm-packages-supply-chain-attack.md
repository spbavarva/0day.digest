---
title: "Multiple Jscrambler Packages Impacted by Supply Chain Attack"
date: 2026-07-14 09:04:39 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/multiple-jscrambler-packages-impacted-by-supply-chain-attack/
---

A threat actor compromised multiple versions of Jscrambler npm packages, poisoning them to drop a cross-platform credential stealer on systems that installed the affected versions. Jscrambler is a JavaScript obfuscation and anti-tampering platform used to protect web and mobile application code, giving the compromised packages a foothold in downstream build pipelines. Details on the exact scope of affected versions and the stealer's capabilities were limited in initial reporting. Developers who installed Jscrambler packages recently should audit for the malicious versions, rotate credentials present on affected build systems, and pin to a known-clean version going forward.
