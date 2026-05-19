---
title: "Microsoft Exchange Zero-Day Under Active Attack, No Patch Available"
date: 2026-05-18 21:43:51 +0000
categories: [Daily Signal]
tags: [zero-day, microsoft, xss, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/vulnerabilities-threats/microsoft-exchange-zero-day-no-patch
---

CVE-2026-42897 is a cross-site scripting vulnerability in Microsoft Exchange's
Outlook Web Access (OWA) that is being actively exploited with no patch
currently available. Successful exploitation allows an attacker to compromise
OWA mailboxes, giving them read and potentially send access to victim email.

Exchange is pervasive in enterprise environments, making this a high-value
target. Organizations running Exchange with OWA exposed should consider
restricting external OWA access or enabling additional authentication controls
while awaiting Microsoft's response. Monitor for unusual OWA login activity or
mail forwarding rules as potential indicators of compromise.
