---
title: "Attackers Target .NET Developers With Poisoned Job Assessments via Malicious NuGet Packages"
date: 2026-11-25 15:48:04 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, nuget]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/threat-intelligence/attackers-net-developers-poisoned-job-assessments
---

Researchers discovered 13 malicious NuGet packages used in a fake
recruitment campaign targeting .NET developers. Victims are lured into a
coding assessment that pulls in the poisoned packages, which spread malware
and give attackers access to the developer's machine.

The campaign is a reminder that job-application workflows are an effective
social engineering vector against developers with access to source code and
build systems. Review any recently added NuGet dependencies pulled in during
take-home assessments.
