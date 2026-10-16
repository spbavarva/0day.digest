---
title: "Attackers Tampered With AOMEI Backupper Update Servers to Deliver Backdoor"
date: 2026-10-16 16:43:39 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html
---

Attackers compromised AOMEI Backupper's own update infrastructure and
repeatedly swapped in malicious files during brief five-to-ten-minute
windows between May and July 2026. Any installation of the Windows backup
program that checked for an update during one of those windows downloaded
and ran a backdoor instead of a legitimate update.

The campaign was identified by Google Threat Intelligence Group, Mandiant,
and ManageEngine's Threat Analysis team. The short, intermittent tampering
windows appear designed to limit exposure while still reaching a subset of
AOMEI Backupper's user base.

Organizations running AOMEI Backupper should check for signs of compromise
on installs that updated during May–July 2026.
