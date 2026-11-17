---
title: "QUIC and Covert: Novel HTTP/3-Powered RATs Target Southeast Asian Governments"
date: 2026-11-16 23:00:55 +0000
categories: [Daily Signal]
tags: [malware, espionage]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/
---

Palo Alto Networks' Unit 42 uncovered a cyberespionage campaign targeting
Southeast Asian government networks using two custom remote access trojans:
PerfectPioneer RAT and the modular KUKURAT. The operators use HTTP/3 (QUIC)
as a covert command-and-control channel, blending malicious traffic with
legitimate encrypted web traffic to complicate network-based detection.

Defenders monitoring government or diplomatic networks in the region should
review QUIC/UDP-443 traffic for anomalous patterns rather than relying
solely on legacy TCP-based inspection.
