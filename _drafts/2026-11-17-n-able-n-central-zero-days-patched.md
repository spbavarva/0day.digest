---
title: "N-able Patches 17 N-central Zero-Days, Some Already Exploited in the Wild"
date: 2026-11-17 12:28:45 +0000
categories: [Daily Signal]
tags: [zero-day, cve, vulnerability]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/n-able-kills-legacy-apis-patches-17-n-central-zero-days/
---

N-able has patched 17 zero-day vulnerabilities in its N-central RMM
platform as part of a release that also removes legacy APIs. Some of the
patched vulnerabilities were already being exploited in the wild before
the fix shipped.

N-central is used by MSPs to remotely manage client endpoints, so
unpatched instances represent a path into every downstream environment an
affected MSP manages. MSPs running N-central should patch immediately and
review for signs of exploitation predating the patch.
