---
title: "Bank Phishing Sites Use Fake 'Suspended' Pages to Evade Takedowns"
date: 2026-11-05 13:22:12 +0000
categories: [Daily Signal]
tags: [phishing]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/bank-phishing-sites-show-fake-suspended-pages-to-evade-takedowns/
---

Researchers found more than 200 phishing sites targeting bank customers
that serve phishing content only to first-time visitors, then show a fake
"suspended" page to anyone who revisits the URL. The technique is designed
to evade takedown crawlers and automated scanners that typically revisit
flagged URLs before acting.

Takedown teams should account for this cloaking behavior when triaging
reported phishing URLs, since a revisit-based scan may falsely clear a
still-active site.
