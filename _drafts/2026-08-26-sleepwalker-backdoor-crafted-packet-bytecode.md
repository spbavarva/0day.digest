---
title: "New SLEEPWALKER Backdoor Waits for One Crafted Packet, Then Runs Its Own Bytecode"
date: 2026-08-26 07:12:55 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html
---

An independent malware researcher documented a previously unreported
Windows backdoor, dubbed SLEEPWALKER, that stays inert in memory until a
specifically crafted network packet reaches the machine, then runs
commands written in a custom 23-instruction bytecode language.

The sample is an unsigned 64-bit DLL (59,904 bytes) built to be
side-loaded, suggesting the operator is prioritizing stealth and
evasion over ease of use.
