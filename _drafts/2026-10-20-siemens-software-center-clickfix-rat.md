---
title: "ClickFix Attackers Exploit Siemens Software Center Flaw to Deploy Remote Access Trojan"
date: 2026-10-20 07:11:45 +0000
categories: [Daily Signal]
tags: [rce, cve, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/clickfix-attackers-exploit-siemens.html
---

Siemens patched a DLL sideloading vulnerability in Siemens Software Center,
tracked as CVE-2026-110936 (CVSS v4 8.4), which it says has been exploited
in ClickFix attacks to deploy a remote access trojan.

The flaw lets an attacker place a malicious DLL in a directory the
application searches, achieving code execution with the application's
privileges. Organizations running Siemens Software Center should patch and
review for ClickFix-style social engineering leading to DLL execution.
