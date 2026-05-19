---
title: "Siemens RUGGEDCOM APE1808 Affected by Critical PAN-OS Captive Portal RCE"
date: 2026-05-19 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce, ics]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-02
---

A buffer overflow in the Palo Alto Networks PAN-OS User-ID Authentication Portal (Captive Portal) allows an unauthenticated attacker to execute arbitrary code with root privileges on PA-Series and VM-Series firewalls by sending specially crafted packets.
This vulnerability affects Siemens RUGGEDCOM APE1808 devices, which embed PAN-OS for OT/ICS environments.
Siemens is preparing fix versions and recommends operators apply Palo Alto Networks' published countermeasures in the interim.
Industrial operators using RUGGEDCOM APE1808 should consult Siemens' upstream advisory and the Palo Alto Networks security notification for available workarounds.
