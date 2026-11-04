---
title: "Debian and Ubuntu APT Flaw Lets MitM Attackers Run Code as Root"
date: 2026-11-04 17:00:46 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation, supply-chain]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html
---

A flaw in APT, the package manager used by Debian and Ubuntu, lets an
attacker who can modify package downloads in transit swap a verified
package for a malicious one. Because APT retries failed downloads by
default starting with Debian 12, an attacker positioned as a
man-in-the-middle can trigger this behavior to get their own package
installed.

The attacker's code then runs as root. Debian, Ubuntu, and APT's developers
published advisories on November 4; patches should be applied as soon as
they're available for your release.
