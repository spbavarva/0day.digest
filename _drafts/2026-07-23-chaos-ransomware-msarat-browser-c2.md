---
title: "Chaos Ransomware's msaRAT Hijacks Chrome and Edge for Covert C2"
date: 2026-07-23 10:00:38 +0000
categories: [Daily Signal]
tags: [ransomware, malware]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/
---

Cisco Talos detailed msaRAT, a new Rust-based implant used by the Chaos
ransomware group ahead of deploying its encryptor. The malware never opens
its own outbound connection; instead it talks only to 127.0.0.1 and drives a
headless Chrome or Edge instance to route command-and-control traffic
through the victim's own browser. Talos says the technique also hides the
attacker's IP via WebRTC over TURN. The implant was found on a compromised
Windows machine ahead of encryption.
