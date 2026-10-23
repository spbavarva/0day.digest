---
title: "Ruby Patches Regex Engine Bugs Behind Four Critical GitLab RCE Flaws"
date: 2026-10-23 17:54:08 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html
---

Ruby released versions 4.0.9, 3.4.12, and 3.3.13 to fix three bugs in
Onigmo, its bundled regular expression engine. The bugs underpin four
critical security flaws that GitLab patched over the past month.

A specially crafted regex pattern could corrupt memory during Ruby's
pattern compilation step, potentially leading to code execution on
GitLab's own servers. Organizations running self-hosted GitLab or other
Ruby applications that compile user-supplied regex should update to the
patched Ruby versions.
