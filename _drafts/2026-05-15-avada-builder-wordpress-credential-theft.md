---
title: "Avada Builder WordPress Plugin Flaws Expose Credentials on 1 Million Sites"
date: 2026-05-15 15:56:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/avada-builder-wordpress-plugin-flaws-allow-site-credential-theft/
---

Two vulnerabilities in the Avada Builder plugin for WordPress — installed on approximately one million active sites — allow attackers to read arbitrary files and extract sensitive information including credentials from the database. An attacker exploiting these flaws could obtain admin credentials, database passwords, and other configuration secrets stored server-side. WordPress administrators running Avada Builder should update to the patched version immediately, rotate any credentials that may have been exposed, and review server access logs for signs of exploitation activity.
