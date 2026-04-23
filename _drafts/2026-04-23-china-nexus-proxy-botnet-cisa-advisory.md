---
title: "CISA and NCSC-UK Warn of China-Nexus APT Using Botnet of Hijacked Consumer Devices"
date: 2026-04-23 12:00:00 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, iam]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-113a
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/uk-warns-of-chinese-hackers-using-botnets-of-hijacked-consumer-devices-to-evade-detection/
---

CISA and NCSC-UK, with support from ASD/ACSC and other Five Eyes partners, published joint
advisory AA26-113a detailing a widespread shift in China-nexus APT tactics: using large proxy
networks built from compromised consumer routers and IoT devices to route malicious traffic and
evade detection. Routing through residential IP addresses defeats geo-blocking controls and
complicates attribution, as the traffic appears to originate from ordinary consumer connections in
target countries.

Defenders should not treat residential or consumer ISP IP ranges as inherently lower-risk for
authentication events, lateral movement, or data access attempts. The advisory includes TTPs and
recommendations for detecting covert proxy usage in enterprise network logs. Organizations should
also audit their own consumer-grade devices and remote-access infrastructure for signs of
compromise that could make them part of such proxy networks.
