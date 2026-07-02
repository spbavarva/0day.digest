---
title: "Critical Cursor Flaws Let Prompt Injection Escape Sandbox"
date: 2026-07-01 14:42:54 +0000
categories: [Daily Signal]
tags: [llm, rce, cve, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
---

Cato AI Labs disclosed two flaws in the Cursor AI code editor, tracked as
CVE-2026-50548 and CVE-2026-50549 and rated 9.8 and 9.3 respectively. Named
DuneSlide, the bugs let a single crafted prompt escape Cursor's sandbox and
execute arbitrary commands on the developer's machine, with no click-through
or approval prompt required. This is a direct prompt-injection-to-RCE chain
against a widely used AI coding tool, not a theoretical jailbreak. Cursor
users should apply the vendor's patch as soon as available and treat
untrusted repository content processed by Cursor as executable input.
