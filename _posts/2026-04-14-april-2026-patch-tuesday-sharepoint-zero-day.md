---
title: "April 2026 Patch Tuesday: SharePoint Zero-Day Among 167 CVEs Fixed"
date: 2026-04-14 21:47:59 +0000
categories: [Daily Signal]
tags: [zero-day, rce, microsoft, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: Krebs on Security
    url: https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/
---

Microsoft released patches for 167 security vulnerabilities, making this the second-largest
Patch Tuesday by CVE count on record. Two zero-days are included: CVE-2026-32201, a SharePoint
Server improper input validation flaw that is under confirmed active exploitation (now added to
CISA's KEV catalog), and a publicly disclosed Windows Defender weakness called "BlueHammer."

Separately, Google Chrome fixed its fourth zero-day of 2026, and Adobe released an emergency
out-of-band patch for an actively exploited Reader flaw enabling remote code execution.

Elevation-of-privilege bugs accounted for more than half the total CVEs patched, with two of
those EoP flaws being zero-days. SharePoint Server instances exposed to the internet should be
treated as highest priority — patch immediately or take offline until patched. Verify Chrome and
Adobe Reader are updated on all endpoints before end of day.
