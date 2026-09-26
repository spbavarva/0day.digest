---
title: "Elementor CSRF Flaw Lets Attackers Take Over WordPress Sites"
date: 2026-09-26 09:55:22 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html
---

A high-severity cross-site request forgery (CSRF) vulnerability in the
Elementor Website Builder WordPress plugin lets an unauthenticated attacker
create a rogue administrator account and take over a site, if an admin
clicks a crafted link. The flaw carries a CVSS score of 8.8 and has not yet
been assigned a CVE identifier.

Site owners running Elementor should watch for a patch and review admin
accounts for unauthorized additions in the meantime.
