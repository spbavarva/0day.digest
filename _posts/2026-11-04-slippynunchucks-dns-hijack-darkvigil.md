---
title: "China-Aligned Hackers Hijack Sogou Input Method DNS to Deploy DarkVigil Backdoor"
date: 2026-11-04 11:24:31 +0000
categories: [Daily Signal]
tags: [malware, dns-hijacking]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html
---

A China-aligned threat actor tracked as SlippyNunchucks is abusing
insecure HTTP communications in the Windows version of Sogou Input Method
to hijack DNS requests. The campaign, observed since July 1, 2026, deploys
a backdoor called DarkVigil (aka FDMTP) as part of a surveillance
operation.

The technique works by intercepting an input method editor's unencrypted
update/config traffic rather than exploiting a traditional software
vulnerability.
