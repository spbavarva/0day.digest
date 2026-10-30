---
title: "CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV Catalog"
date: 2026-10-30 07:27:05 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html
---

CISA added two actively exploited vulnerabilities to its Known Exploited
Vulnerabilities catalog: a GitLab flaw and a Cisco firewall
denial-of-service bug.

CVE-2026-97229 is an integer overflow/wraparound vulnerability in GitLab
Community and Enterprise Edition carrying a CVSS score of 10.0, and allows
unauthenticated attackers to execute arbitrary code on the server. It has
also been observed exploited against Alpine Linux deployments
specifically.

The Cisco firewall flaw added alongside it causes denial of service;
CISA's advisory did not specify the Cisco product line or CVE details
beyond the KEV listing.

Organizations running affected GitLab or Cisco firewall versions should
prioritize patching per CISA's KEV deadlines.
