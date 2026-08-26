---
title: "Unpatched Kaltura mwEmbed Flaws Could Let Remote Attackers Read Files and Run Code"
date: 2026-08-26 11:55:00 +0000
categories: [Daily Signal]
tags: [cve, rce, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/unpatched-kaltura-mwembed-flaws-could.html
---

CERT/CC disclosed two unpatched vulnerabilities in Kaltura's mwEmbed
HTML5 video player library, tracked as CVE-2026-19913 and
CVE-2026-19912. Both stem from unsafe deserialization in the
mwEmbedLoader.php endpoint and allow a remote, unauthenticated attacker
to read arbitrary files and execute code.

Since no patch is currently available, sites embedding the mwEmbed
player should look for compensating controls, such as restricting
access to the vulnerable endpoint, until a fix ships.
