---
title: "CISA ICS Advisories: ABB Edgenius CVSS 9.6 Auth Bypass and Five Additional ABB Product Flaws"
date: 2026-04-30 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, ics]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-120-03
---

CISA published six ICS advisories today covering ABB industrial products. The most critical is ABB Edgenius Management Portal (CVSS 9.6) — an authentication bypass allowing arbitrary code installation, application uninstallation, and full configuration modification on affected portal instances. ABB Ability OPTIMAX (CVSS 8.1) carries an Azure AD SSO authentication bypass affecting versions 6.1 through 6.4. ABB System 800xA and Symphony Plus IEC 61850 products have a remote crash vulnerability; ABB PCM600 has a path traversal flaw (CVSS 4.4).

Organizations running ABB ICS in critical manufacturing, energy, or utilities should prioritize patching Edgenius Management Portal (versions 3.2.0.0 and 3.2.1.1) and OPTIMAX (versions prior to 6.3.1-251120 / 6.4.1-251120) first. Where network segmentation exists, confirm IEC 61850 management interfaces are not internet-reachable.
