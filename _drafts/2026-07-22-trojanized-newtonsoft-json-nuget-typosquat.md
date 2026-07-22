---
title: "Trojanized Newtonsoft.Json Fork Found on NuGet"
date: 2026-07-22 06:00:06 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/trojanized-newtonsoftjson-fork-hides.html
---

Researchers discovered a NuGet typosquat package, "Newtonsoftt.Json.Net,"
that mimics the popular Newtonsoft.Json library as a trojanized fork.
Rather than the info-stealer payloads typical of package-registry malware,
this package is designed to rig live game results on the Digitain
platform. Seven versions of the package have been published to NuGet.
Developers should double-check package names before installing dependencies.
