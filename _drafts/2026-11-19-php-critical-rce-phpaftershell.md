---
title: "PHP Patches 18 Flaws, Including Critical 'phpAfterShell' RCE Chain"
date: 2026-11-19 16:28:23 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html
---

The PHP Foundation shipped security updates fixing 18 vulnerabilities,
including several critical flaws that could let unauthenticated attackers
execute code on vulnerable servers. The most notable, dubbed
"phpAfterShell" and tracked as CVE-2026-126714, abuses PHP's default
file-based session storage: cutting off a session write at the right
moment lets an attacker make PHP return attacker-chosen objects, which
combined with a suitable gadget chain in the app can lead to remote code
execution. Exploitability depends heavily on app configuration — experts
quoted by Dark Reading cautioned against "PHP2Shell"-style panic. Admins
running PHP should still apply this month's release.
