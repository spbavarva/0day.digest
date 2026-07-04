---
title: "Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices"
date: 2026-07-03 20:19:31 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, supply-chain, embedded-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
---

Security firm runZero disclosed seven vulnerabilities in FatFs, a lightweight
filesystem library that lets embedded devices read and write FAT and exFAT
storage such as USB drives and SD cards. FatFs ships inside firmware for
security cameras, drones, industrial controllers, hardware crypto wallets,
and many other embedded systems, giving the flaws broad reach. The
vulnerabilities are described as unpatched at time of disclosure.
Organizations building or maintaining FatFs-based firmware should watch for
an upstream fix and review exposure of FAT/exFAT-parsing code paths on their
devices.
