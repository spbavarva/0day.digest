---
title: "Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode"
date: 2026-08-25 12:43:51 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html
---

Marimo patched a high-severity flaw in its notebook software that let an
attacker-supplied Model Context Protocol (MCP) command execute as a local
subprocess when a specially crafted notebook was opened in edit mode, before
any cell actually ran. The issue was assigned a CVE via VulnCheck's CNA.
Because MCP commands are meant to extend AI agent tooling inside the
notebook, an attacker could use a shared or downloaded notebook file to get
arbitrary local code execution on anyone who opens it in edit mode. Users
should update Marimo and treat untrusted notebook files as executable
content rather than passive documents.
