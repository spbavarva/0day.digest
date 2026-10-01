---
title: "Scan Finds 500,000 Active Credentials Exposed on GitHub"
date: 2026-10-01 09:43:56 +0000
categories: [Daily Signal]
tags: [data-breach, github, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/500000-active-credentials-left-exposed-on-github/
---

A scan identified roughly 500,000 active credentials exposed in public
GitHub repositories. About 200,000 of those were only discovered after
GitHub enabled secret-scanning push protection by default. The summary does
not name the organization behind the scan or specify credential types.
Developers should rotate any secrets that may have been committed to source
control and enable push protection on their own repositories.
