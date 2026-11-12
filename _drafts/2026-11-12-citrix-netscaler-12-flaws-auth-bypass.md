---
title: "Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass"
date: 2026-11-12 15:38:49 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html
---

Citrix released patches for multiple critical flaws in NetScaler ADC,
NetScaler Gateway, and NetScaler Console that could lead to denial-of-
service or an authentication bypass.

The most severe, CVE-2026-120868 (CVSS 9.3), is a memory overflow
vulnerability in packet processing. Given NetScaler's history as an active
exploitation target, admins should prioritize patching ADC and Gateway
deployments.
