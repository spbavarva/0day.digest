---
title: "CISA Orders Federal Agencies to Patch Actively Exploited Ivanti Sentry RCE Within 3 Days"
date: 2026-06-12 08:26:55 +0000
categories: [Daily Signal]
tags: [zero-day, rce, vulnerability, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/
  - name: SecurityWeek
    url: https://www.securityweek.com/ivanti-sentry-exploitation-attempts-hitting-honeypots/
---

CISA issued Binding Operational Directive (BOD) 26-04, ordering federal
agencies to patch an actively exploited critical OS command injection
vulnerability in Ivanti Sentry within three days. The flaw allows attackers to
execute arbitrary code with root privileges.

SecurityWeek reports that exploitation attempts targeting the vulnerability
are already hitting honeypots, indicating scanning activity well beyond the
federal directive's scope.

Organizations running Ivanti Sentry should patch immediately rather than wait
on the federal deadline, and review logs for command-injection indicators.
