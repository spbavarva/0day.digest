---
title: "Datasette Patches Table Permission Bypass Exposing Private Rows"
date: 2026-09-16 23:51:08 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Sep/16/datasette-2/
---

Datasette shipped a security fix in 0.65.5 (also included in 1.0a40) for
a bug where a trailing newline in a requested table name could bypass
table permissions and expose private rows. The issue was reported by
dpfkdlemtp and is tracked as GHSA-h547-rmjf-5m2m.

Datasette is a widely used open-source tool for exploring and publishing
data. Users running it with table-level permissions should upgrade to a
patched version.
