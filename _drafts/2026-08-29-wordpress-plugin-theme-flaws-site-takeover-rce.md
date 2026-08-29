---
title: "Five Critical WordPress Plugin and Theme Flaws Enable Site Takeover or RCE"
date: 2026-08-29 16:25:03 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce, wordpress]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html
---

Wordfence and Patchstack disclosed five critical flaws across popular
WordPress plugins and themes: WPMU DEV Dashboard, Avada, TranslatePress,
Pods, and GiveWP. The most severe, CVE-2026-76581 (CVSS 9.8), is an
authentication bypass flaw.

Depending on the plugin, the issues can lead to authentication bypass,
account takeover, or arbitrary code execution. Site operators running
any of the affected plugins or themes should update to patched versions
as soon as they're available.
