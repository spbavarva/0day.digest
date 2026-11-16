---
title: "BO Team Exploits Log4Shell in VMware vCenter, Compromises Russian Firm's Code-Signing Server"
date: 2026-11-16 06:53:34 +0000
categories: [Daily Signal]
tags: [rce, supply-chain, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/bo-team-exploits-log4shell-in-vmware.html
---

Kaspersky's ICS CERT team uncovered a months-long compromise of a Russian
software developer's network, including its code-signing server, following
exploitation of the Log4Shell vulnerability in VMware vCenter. The intrusion
is attributed to a threat actor tracked as BO Team (aka Black Owl, Hoody
Hyena).

Access to a code-signing server lets an attacker sign malicious binaries as
legitimate, creating downstream supply chain risk for the developer's
customers. The compromise was discovered after the affected developer
contacted Kaspersky in June 2025.
