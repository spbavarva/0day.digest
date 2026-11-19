---
title: "Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT"
date: 2026-11-19 19:21:06 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
---

Google says a China-linked espionage group exploited a critical VMware
vCenter authentication bypass as a zero-day before Broadcom shipped a
patch. The flaw, rated CVSS 9.8, lets a network-positioned attacker bypass
authentication entirely and gain unauthorized access to vCenter — the
central console for managing an organization's ESXi hosts and virtual
machines. Broadcom has released fixes for all supported branches and
lists no workaround. Organizations running vCenter should patch
immediately and review logs for signs of prior compromise given the
confirmed in-the-wild exploitation.
