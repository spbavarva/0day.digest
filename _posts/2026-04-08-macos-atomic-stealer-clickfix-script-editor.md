---
title: "Atomic Stealer Delivered to macOS Users via ClickFix Script Editor Attack"
date: 2026-04-08 18:55:43 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-macos-stealer-campaign-uses-script-editor-in-clickfix-attack/
---

A new campaign distributes Atomic Stealer to macOS users by abusing macOS Script Editor in a ClickFix-style attack — tricking users into copy-pasting and running malicious Terminal commands. The technique routes execution through a trusted system application, bypassing Gatekeeper.

This is an adaptation of the ClickFix social engineering pattern previously common on Windows, now ported to macOS. Security teams should add detections for unusual Script Editor to Terminal execution chains, and security awareness training should cover prompts that instruct users to run terminal commands.
