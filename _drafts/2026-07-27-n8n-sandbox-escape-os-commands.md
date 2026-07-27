---
title: "n8n Sandbox Escape Lets Workflow Editors Run OS Commands"
date: 2026-07-27 13:05:15 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/n8n-sandbox-escape-lets-workflow.html
---

n8n has patched a high-severity expression-sandbox escape that let an
authenticated workflow editor execute operating-system commands on the
server running the automation platform. Security Joes discovered the flaw
while re-examining n8n's February fix for CVE-2026-27577 for a possible
bypass. Affected versions are below 2.31.5 and from 2.32.0 up to but not
including 2.32.1; fixes have shipped in 2.31.5 and later. Organizations
self-hosting n8n should update and review workflow-editor permissions given
the sandbox bypass.
