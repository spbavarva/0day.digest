---
title: "BRIDGE:BREAK — 22 Flaws in Lantronix and Silex Serial-to-IP Converters, 20,000 Devices Exposed"
date: 2026-04-21 15:46:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, iot, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/22-bridgebreak-flaws-expose-20000.html
---

Forescout Research Vedere Labs has disclosed BRIDGE:BREAK, a collection of 22 vulnerabilities
across Lantronix and Silex serial-to-IP converter models. Nearly 20,000 devices are internet-
exposed, enabling mass exploitation. The flaws allow attackers to hijack converters and tamper
with data transiting between legacy serial equipment and IP networks.

Serial-to-Ethernet converters are common in industrial, healthcare, and critical infrastructure
settings — they act as bridges connecting legacy OT/ICS serial devices (PLCs, sensors, meters)
to modern IP infrastructure. Compromise gives an attacker a foothold into systems that would
otherwise be unreachable from IP networks, undermining assumed air-gap protections.

Affected products span multiple Lantronix and Silex product lines. Vendor patches are expected,
but OT patch cycles are often measured in months or years. The immediate mitigation is to take
these converters off internet-facing interfaces, enforce firewall rules at the IT/OT boundary,
and monitor for unexpected serial-to-IP traffic anomalies.
