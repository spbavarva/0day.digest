---
title: "Critical cPanel Flaw Lets Hosting Customer Take Root Control of Shared Server"
date: 2026-08-28 09:45:15 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html
---

cPanel released patches for CVE-2026-65643, a critical vulnerability in
domain parking and addon domain functionality in cPanel and WebHost Manager
(WHM) that could let a hosting customer execute code as the root user,
taking over the entire shared server. The flaw impacts all supported
versions of cPanel & WHM. Hosting providers should apply the patch
promptly, since on shared hosting a single malicious or compromised
customer account could otherwise compromise every other tenant on the box.
