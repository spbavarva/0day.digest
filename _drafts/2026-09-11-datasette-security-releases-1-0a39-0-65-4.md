---
title: "Datasette 1.0a39 and 0.65.4 Security Releases"
date: 2026-09-11 03:27:16 +0000
categories: [Daily Signal]
tags: [appsec, vulnerability]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Sep/11/datasette-security/
---

Datasette shipped two security patch releases, 1.0a39 for the alpha series
and 0.65.4 for the stable line, fixing issues reported by external
researchers. The vulnerabilities specifically affect instances that mix
public and private tables on the public web, which could expose data meant
to stay private. Maintainer Simon Willison said the fixes followed an
extensive audit and about a week of review before release. Anyone running a
public Datasette instance with mixed public/private tables should upgrade
immediately.
