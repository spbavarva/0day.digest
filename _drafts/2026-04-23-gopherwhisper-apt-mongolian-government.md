---
title: "GopherWhisper: China-Linked APT Backdoors 12 Mongolian Government Systems"
date: 2026-04-23 09:04:00 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/china-linked-gopherwhisper-infects-12.html
---

ESET researchers uncovered GopherWhisper, a previously undocumented China-aligned APT active
since at least November 2023, which infected 12 Mongolian government institutions. The group
deploys a custom Go-based toolkit using injectors and loaders to plant and execute multiple
backdoors, discovered in January 2025 when investigators found an unknown backdoor on a Mongolian
government network. Command and control runs through Microsoft 365 Outlook, Slack, and Discord —
legitimate cloud services that blend attacker traffic with normal enterprise communication flows.

Organizations should monitor for anomalous OAuth token activity on collaboration platforms and
watch for Go-compiled binaries in unexpected process trees or file paths. Unusual API calls to
Outlook, Slack, or Discord from server-side processes warrant investigation. Government and
diplomatic entities in Central Asia appear to be the primary target profile.
