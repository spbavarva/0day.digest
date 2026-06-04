---
title: "APT Group Silently Exfiltrated Stock Exchange Executive's Inbox for Five Months"
date: 2026-06-04 09:33:57 +0000
categories: [Daily Signal]
tags: [data-breach, malware, iam]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html
---

Unknown attackers maintained persistent access to the Outlook mailbox of a
senior executive at a major global stock exchange for at least five months,
exfiltrating inbox contents in small repeated batches. Data was routed through
Dropbox and OneDrive to blend with normal cloud activity, obscuring the
exfiltration channel. Symantec and Carbon Black's Threat Hunter Team attributed
the campaign to espionage rather than financial theft. The extended dwell time
and abuse of legitimate cloud storage for exfiltration are consistent with
nation-state tradecraft. Security teams should monitor for anomalous OAuth
authorizations, Outlook delegation rules, and bulk mail forwarding targeting
executive accounts.
