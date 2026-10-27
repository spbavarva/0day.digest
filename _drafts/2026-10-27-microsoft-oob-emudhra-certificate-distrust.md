---
title: "Microsoft Ships Out-of-Band Windows Updates to Distrust eMudhra Certificates"
date: 2026-10-27 18:20:28 +0000
categories: [Daily Signal]
tags: [vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-oob-updates-to-distrust-emudhra-certificates/
---

Microsoft released out-of-band Windows updates to remove trust in
certificates tied to compromised keys from certificate authority eMudhra.
The updates protect systems that don't automatically receive routine
certificate trust list updates.

Organizations relying on eMudhra-issued certificates should verify their
systems have received the OOB update, since the affected CA keys could
otherwise be used to issue fraudulent trusted certificates. Further
detail on the scope of the eMudhra compromise was not available in
initial reporting.
