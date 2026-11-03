---
title: "Trail of Bits Uses Codex to Backport 149 CVE Fixes Into Stable Linux Kernel Releases"
date: 2026-11-02 12:00:00 +0000
categories: [Daily Signal]
tags: [appsec, llm, devsecops, openai]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/
---

Trail of Bits is using OpenAI's Codex to automate backporting security
fixes into stable Linux distributions, cutting a process that normally
takes days down to hours per fix. By October 29, the project had
helped land fixes for 149 distinct CVEs into stable Linux kernel
releases, plus additional fixes for Fedora and Ubuntu packages.

The work targets a long-standing problem: fixes often don't reach LTS
kernels and distro packages because backporting is slow, manual work.
It's a concrete example of AI tooling applied directly to defensive
security maintenance at scale.
