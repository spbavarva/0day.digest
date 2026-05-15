---
title: "TrickMo Android Banker Adopts TON Blockchain for Covert C2 Communications"
date: 2026-05-11 09:03:02 +0000
categories: [Daily Signal]
tags: [malware, android]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/trickmo-android-banker-adopts-ton-blockchain-for-covert-comms/
---

A new TrickMo variant targeting banking users across Europe has adopted The Open Network (TON)
blockchain as its command-and-control channel. By routing C2 traffic through a decentralized
network, the variant makes traditional sinkholing and infrastructure takedowns significantly
harder compared to centralized C2 servers.

The new build adds commands beyond TrickMo's standard overlay-attack and credential-theft
capabilities. Using blockchain infrastructure for C2 is an emerging evasion technique observed
in a small number of mobile malware families. Security teams protecting European financial
sector employees should update mobile threat defense detections to flag TON network connections
from non-TON applications and watch for TrickMo's characteristic overlay activity on banking
apps.
