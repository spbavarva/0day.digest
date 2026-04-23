---
title: "UAT-4356 Exploits Cisco Firepower Devices with FIRESTARTER Backdoor"
date: 2026-04-23 15:10:57 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, cve, rce]
severity: high
must_know: false
sources:
  - name: Cisco Talos
    url: https://blog.talosintelligence.com/uat-4356-firestarter/
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/analysis-reports/ar26-113a
---

Cisco Talos and CISA published joint details on UAT-4356, an APT group actively exploiting
CVE-2025-20333 and CVE-2025-20362 in Cisco Firepower eXtensible Operating System (FXOS) to
install the FIRESTARTER backdoor for persistent access. The targeted devices include publicly
accessible Cisco Firepower, ASA, and FTD appliances. CISA's malware analysis report (AR26-113a)
assesses that advanced persistent threat actors are using FIRESTARTER specifically for persistence
on internet-facing firewall infrastructure, with UK NCSC co-attributing the campaign.

Cisco appliance operators should apply patches for both CVEs immediately. Review management access
logs on Firepower and ASA devices for signs of unauthorized activity, and consult the CISA MAR for
FIRESTARTER indicators of compromise to use in endpoint and network detection rules.
