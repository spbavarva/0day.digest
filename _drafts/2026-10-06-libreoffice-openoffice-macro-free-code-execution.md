---
title: "LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without Macro Warnings"
date: 2026-10-06 11:57:00 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html
---

Security researchers showed that a malicious spreadsheet can make
LibreOffice and Apache OpenOffice execute attacker-controlled code as soon as
the file is opened — with none of the macro-warning prompts both programs
normally show before running macro code. The attack only works when the
program's Java support is enabled. So far it has only been demonstrated as a
proof of concept, with no reports of in-the-wild use. Organizations that
don't need Java support in LibreOffice/OpenOffice should consider disabling
it as a mitigation.
