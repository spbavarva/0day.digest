---
title: "E4del and PINHOLE RATs Turn FTP Banners Into Dead Drops for Malware Commands"
date: 2026-08-25 11:33:44 +0000
categories: [Daily Signal]
tags: [malware, rce]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html
---

Researchers identified a new campaign delivering two previously unreported
remote access trojans, tracked as E4del and PINHOLE, which use FTP server
banners as dead drop resolvers (DDRs) for command-and-control. Abusing
legitimate services to host or point to C2 infrastructure is a known
technique for blending in with normal network traffic, but using FTP banner
text specifically as the drop point for commands is a less common variant.
The malware families and their full capabilities are still being profiled.
Defenders should treat unexpected FTP banner-grabbing behavior from
endpoints as a potential C2 signal worth investigating.
