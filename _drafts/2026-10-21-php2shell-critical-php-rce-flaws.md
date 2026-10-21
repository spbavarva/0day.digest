---
title: "PHP2Shell: Emergency Patches for Two Critical Unauthenticated RCE Flaws in Core PHP"
date: 2026-10-21 14:00:00 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, zero-day, wiz]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
---

PHP shipped emergency out-of-cycle patches for two critical vulnerabilities in
the PHP runtime itself — CVE-2026-109618 and CVE-2026-109619, dubbed
PHP2Shell — that allow unauthenticated remote code execution and memory
disclosure on any affected server. Fixes landed in PHP 8.5.12, 8.4.27,
8.3.36, and 8.2.35. Because the flaws sit in core PHP rather than application
code, every site on an unpatched version is exposed regardless of its own
security posture.

Details leaked prematurely on forums and social media the day before the
scheduled release, and several security vendors reported exploitation
attempts in the window around disclosure, though CISA said it had not
confirmed in-the-wild exploitation as of its alert. Wiz Research, working
with Google Cloud's Gemini 4 Argon model, is credited with finding and
helping validate the fix.
