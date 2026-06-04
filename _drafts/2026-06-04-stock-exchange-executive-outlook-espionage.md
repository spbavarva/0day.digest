---
title: "Attackers Spent Five Months in Stock Exchange Executive's Outlook Mailbox"
date: 2026-06-04 09:33:57 +0000
categories: [Daily Signal]
tags: [data-breach, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html
---

Symantec and Carbon Black's Threat Hunter Team identified a prolonged espionage campaign in which unknown attackers maintained persistent access to a senior executive's Outlook mailbox at a major global stock exchange for at least five months. Email was exfiltrated in small, repeated batches routed through Dropbox and OneDrive to blend with normal cloud traffic and evade destination-based DLP detection. The technique highlights how attackers use sanctioned cloud services for exfiltration to avoid triggering reputation-based alerts; behavioral DLP that flags unusual volumes rather than unusual destinations would be more effective here.
