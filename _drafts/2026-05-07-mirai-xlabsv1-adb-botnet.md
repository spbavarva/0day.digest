---
title: "Mirai-Derived xlabs_v1 Botnet Hijacks IoT Devices via Exposed Android Debug Bridge"
date: 2026-05-06 20:21:00 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, iot, ddos]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/mirai-based-xlabsv1-botnet-exploits-adb.html
---

Hunt.io researchers uncovered a new Mirai-derived botnet, self-identified as xlabs_v1, that exploits internet-exposed Android Debug Bridge (ADB) interfaces to compromise IoT and Android devices. The botnet enlists hijacked devices into a DDoS-capable network. The campaign was discovered after researchers identified an exposed directory on a Netherlands-hosted server. Device owners and network operators should ensure ADB interfaces are disabled or firewall-blocked on any internet-facing IoT or Android hardware.
