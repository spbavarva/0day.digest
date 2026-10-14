---
title: "AI Pentesting Agent Finds Critical OTP Bypass in Production Insurance System"
date: 2026-10-14 11:00:00 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/an-ai-agent-found-critical-otp-bypass.html
---

During an authorized assessment, an AI pentesting agent independently
discovered a critical authentication bypass on a major insurer's
production website.

The flaw let an attacker choose where a one-time passcode was delivered
during login, effectively letting them redirect the OTP to an address they
controlled.

Finding the bug was described as straightforward; safely proving
exploitability on a live production system without disrupting service was
the harder part of the engagement.
