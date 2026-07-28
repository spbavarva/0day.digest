---
title: "Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root"
date: 2026-07-28 12:56:14 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html
---

OpenWrt shipped version 24.10.8 to fix a critical stack overflow in its
DHCPv6 server (odhcpd), tracked as CVE-2026-53921 with a CVSS score of 9.8.
The flaw lets an unauthenticated attacker who can reach the DHCPv6 service
overwrite a stack buffer via a crafted request, potentially achieving code
execution as root. The release also addresses a wider set of remotely
triggerable flaws in network services enabled by default. Devices on
affected OpenWrt versions should be updated as soon as possible.
