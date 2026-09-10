---
title: "Gigabud Banking Trojan Uses Android Work Profiles to Evade Malware Checks"
date: 2026-09-10 11:33:43 +0000
categories: [Daily Signal]
tags: [malware, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/gigabud-creates-android-work-profiles.html
---

The Gigabud Android banking trojan now installs a second app that creates a
work profile on infected phones, then drops a tampered banking app inside
that isolated space, according to Group-IB. Because Android work profiles
are typically reserved for employer-managed apps kept separate from the
personal space, the technique helps the malware evade banking apps'
malware checks.

Users should be cautious of apps requesting creation of a work profile
outside an enterprise MDM context.
