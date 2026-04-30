---
title: "Forescout Finds Tens of Thousands of Exposed RDP and VNC Servers Tied to ICS/OT"
date: 2026-04-29 12:03:40 +0000
categories: [Daily Signal]
tags: [vulnerability, ics, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/hundreds-of-internet-facing-vnc-servers-expose-ics-ot/
---

Forescout identified tens of thousands of internet-exposed RDP and VNC servers that can be mapped to specific industries, with hundreds directly linked to ICS and OT environments. Remote desktop protocols on operational technology networks represent a critical attack surface: a single compromised endpoint can give attackers direct access to industrial control systems.

Organizations with OT environments should immediately audit externally reachable remote access services, apply strict network segmentation between IT and OT zones, and enforce multi-factor authentication on any VNC or RDP instances that must remain reachable. Internet-exposed RDP/VNC on ICS networks is an elementary misconfiguration — the persistence of this exposure at scale reflects a patching and asset-visibility gap in many industrial operators.
