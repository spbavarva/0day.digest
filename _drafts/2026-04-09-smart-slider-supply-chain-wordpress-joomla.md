---
title: "Smart Slider 3 Pro Update System Hijacked to Deliver Backdoored WordPress and Joomla Versions"
date: 2026-04-09 16:15:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, wordpress, appsec]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/smart-slider-updates-hijacked-to-push-malicious-wordpress-joomla-versions/
---

Attackers compromised the update delivery system for Smart Slider 3 Pro, a popular plugin
for WordPress and Joomla, and pushed a malicious version containing multiple backdoors to
sites with auto-update enabled. The attack targets the distribution mechanism rather than
a code vulnerability, making it a classic software supply chain compromise.

Site owners that received the trojanized update have likely granted attackers persistent
server-side access. All sites running Smart Slider 3 Pro should audit their installation
for signs of the malicious version, check file integrity, and rotate all server credentials
and database passwords. Disable automatic plugin updates until the vendor confirms the
update pipeline is clean and re-secured. Forensic review of web server logs around the
update window is recommended to assess whether backdoors were invoked.
