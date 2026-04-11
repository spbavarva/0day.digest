---
title: "GlassWorm Campaign Uses Zig Dropper to Infect All IDEs on Developer Machines"
date: 2026-04-10 13:23:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, appsec]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/glassworm-campaign-uses-zig-dropper-to.html
---

The GlassWorm campaign has introduced a Zig-language dropper distributed as a malicious
Open VSX extension named "specstudio.code-wakatime-activity-tracker," impersonating the
legitimate WakaTime time-tracking plugin. Once installed, the dropper targets and
infects every IDE found on the developer's machine. The use of Zig makes the dropper
harder to flag with conventional signature-based detection. Developers using VS Code or
any Open VSX-compatible editor should audit installed extensions immediately, verify
any WakaTime-related extension is published by the official wakatime publisher, and
remove any unfamiliar or recently installed activity-tracker extensions. IDE infection
gives attackers persistent access to source code, credentials, and build pipelines.
