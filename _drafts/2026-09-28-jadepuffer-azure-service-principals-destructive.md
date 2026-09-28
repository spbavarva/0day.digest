---
title: "JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources"
date: 2026-09-28 09:08:21 +0000
categories: [Daily Signal]
tags: [azure, cloud-security, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
---

The threat actor JADEPUFFER, tracked by Microsoft as Storm-3168, used
compromised Azure service principals to carry out destructive operations
inside a victim's Azure environment, deleting resources over roughly 18
hours in early June 2026. Microsoft describes it as an evolution of the
group's tradecraft.

Details on how the service principals were initially compromised were not
included in the source summary. Organizations should audit service
principal credentials and permissions and monitor for anomalous
resource-deletion activity.
