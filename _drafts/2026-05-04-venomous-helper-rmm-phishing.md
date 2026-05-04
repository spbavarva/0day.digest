---
title: "VENOMOUS#HELPER: Phishing Campaign Abuses RMM Tools to Persist in 80+ Organizations"
date: 2026-05-04 18:06:00 +0000
categories: [Daily Signal]
tags: [phishing, malware, rmm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html
---

An ongoing phishing campaign tracked as VENOMOUS#HELPER has targeted over 80 organizations, primarily in the U.S., since at least April 2025. After initial phishing compromise, attackers deploy legitimate Remote Monitoring and Management tools — specifically SimpleHelp and ScreenConnect — to establish persistent remote access to victim hosts.

Using legitimate RMM software allows attackers to blend into managed service provider and IT operations traffic, significantly complicating detection. The campaign shares overlaps with previously tracked threat clusters according to Securonix. Security teams should audit for unexpected RMM agent deployments, enforce application allowlisting policies that control which RMM tools are permitted, and correlate any new RMM agent installs with known IT change requests.
