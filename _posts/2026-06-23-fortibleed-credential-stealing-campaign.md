---
title: "FortiBleed Attackers Use Golang Sniffer to Harvest 110 Million Credentials"
date: 2026-06-23 12:34:54 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, data-breach]
severity: critical
must_know: true
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/fortibleed-attackers-firewalls-credentials-stealers
  - name: SecurityWeek
    url: https://www.securityweek.com/russian-initial-access-broker-behind-fortibleed-campaign/
---

A threat actor is running an ongoing credential-harvesting campaign against
FortiGate firewalls using a custom Golang-based sniffer. The campaign has
targeted roughly 430,000 FortiGate firewalls and captured an estimated 110
million credentials since at least February 2026. SecurityWeek attributes the
activity to a Russian initial access broker, and the heists are described as
still persisting. Organizations running FortiGate firewalls should audit for
signs of credential sniffing and rotate any potentially exposed credentials.
