---
title: "AI Used to Reconstruct Dead Pilots' Voices from NTSB Cockpit Recordings"
date: 2026-05-22 23:03:33 +0000
categories: [Daily Signal]
tags: [ai-safety, llm, appsec]
severity: medium
must_know: false
sources:
  - name: TechCrunch AI
    url: https://techcrunch.com/2026/05/22/ai-is-being-used-to-resurrect-the-voices-of-dead-pilots/
---

Researchers used AI on spectrogram images of NTSB cockpit voice recordings to
reconstruct intelligible audio of deceased pilots — a technique the agency had
not anticipated. The reconstruction was compelling enough that the NTSB
temporarily blocked public access to its online docket system while it assessed
the implications.

This is a practical example of AI defeating redaction-by-obscurity: audio
converted to a visual format was assumed safe to share, but ML-based
spectrogram-to-audio inversion made recovery straightforward. Organizations
publishing sanitized media artifacts should treat spectrogram images, waveform
exports, and similar derivatives as potentially reversible.
