---
title: "Trojanized Newtonsoft.Json Fork on NuGet Rigs Game Outcomes"
date: 2026-07-22 06:00:06 +0000
categories: [Daily Signal]
tags: [supply-chain, nuget]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/trojanized-newtonsoftjson-fork-hides.html
---

Researchers found a NuGet typosquat, "Newtonsoftt.Json.Net," that
masquerades as the widely used Newtonsoft.Json library. Unlike typical
info-stealer typosquats, this is a working trojanized fork built to rig
live game results on the gambling platform Digitain rather than exfiltrate
data. Seven versions of the package have been published so far. Because it
behaves as a functional drop-in replacement for the real library, it's
harder to catch in a routine dependency review than a package that fails
to work. Teams should double-check package names and publishers before
adding Newtonsoft.Json-like dependencies.
