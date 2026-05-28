---
title: "CISA Warns of Frontier X Medical Device Flaw That Could Allow Attackers to Alter Clinical Readings"
date: 2026-05-28 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, iam]
severity: high
must_know: false
sources:
  - name: CISA
    url: https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-148-01
---

CISA advisory ICSMA-26-148-01 covers a missing authentication flaw (CVSS 8.8)
in the Fourth Frontier Frontier X cardiac monitoring device. Successful exploitation
allows an attacker to read and write arbitrary Bluetooth handle values and alter
clinical readings, potentially taking control of the device and causing patient
harm. Affected versions include Frontier X Android app below v15.0.0, iOS app
below v25.0.0, and all versions of Frontier X2. Healthcare providers using Frontier
X devices should apply the vendor updates immediately and review device exposure
to untrusted Bluetooth environments.
