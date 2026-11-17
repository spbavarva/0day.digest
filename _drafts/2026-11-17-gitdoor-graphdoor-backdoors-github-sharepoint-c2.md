---
title: "New GitDoor and GraphDoor Backdoors Abuse GitHub and SharePoint for Covert C2"
date: 2026-11-17 11:20:18 +0000
categories: [Daily Signal]
tags: [malware, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html
---

Kaspersky disclosed two previously undocumented backdoors, GitDoor and
GraphDoor, used in a campaign it calls Operation ShadowCloud, targeting
government sectors in Asia and Africa. Both backdoors abuse legitimate
services — GitHub and Microsoft SharePoint — as covert command-and-control
channels, letting malicious traffic blend in with normal developer and
enterprise activity.

Kaspersky says it identified the campaign in early 2026. Defenders
monitoring for C2 should include GitHub and SharePoint API traffic
patterns in detection coverage rather than assuming traffic to these
services is inherently benign.
