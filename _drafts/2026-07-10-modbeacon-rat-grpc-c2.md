---
title: "New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic"
date: 2026-07-10 13:15:23 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html
---

The China-linked cybercrime group Silver Fox has been linked to a new
Rust-based remote access trojan called MODBEACON, which uses gRPC
streaming to encrypt its command-and-control traffic. Chinese security
firm QiAnXin notes that while the group's activity can look like
low-sophistication, high-volume operations relying on counterfeit
installers and SEO poisoning to spread malware, the underlying tooling
reflects a more organized operation. Defenders should be aware that
gRPC-based C2 can blend in with legitimate application traffic,
complicating network-based detection.
