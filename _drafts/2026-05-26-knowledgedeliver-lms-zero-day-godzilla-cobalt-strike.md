---
title: "KnowledgeDeliver LMS Zero-Day Exploited to Deploy Godzilla Web Shell and Cobalt Strike"
date: 2026-05-26 05:19:38 +0000
categories: [Daily Signal]
tags: [zero-day, rce, vulnerability, cve, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/knowledgedeliver-lms-flaw-exploited-to.html
---

CVE-2026-5426 (CVSS 7.5), a now-patched flaw in Digital Knowledge's KnowledgeDeliver LMS—widely used in Japan—was exploited as a zero-day before a patch was available. The vulnerability stems from hardcoded ASP.NET machine keys in configuration files, enabling ViewState deserialization attacks that lead to unauthenticated remote code execution.

Attackers used the flaw to deploy the Godzilla web shell and subsequently load Cobalt Strike Beacon for post-exploitation. Organizations running KnowledgeDeliver should apply the patch immediately, audit web server logs for ViewState deserialization activity, and hunt for Godzilla or Cobalt Strike artifacts in the environment.
