---
title: "Datasette SQL Injection Fix (1.0a38)"
date: 2026-08-06 18:24:34 +0000
categories: [Daily Signal]
tags: [sqli, vulnerability]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Aug/6/datasette/#atom-everything
---

Datasette 1.0a38 (backported to 0.65.3) fixes a SQL injection vulnerability
affecting instances that serve a mix of public and private tables in the same
database using Datasette's permissions system. Even with the execute-sql
permission disabled, a user with access to any public table could exploit the
bug to run SQL injection attacks and reach private tables. Site administrators
serving mixed public/private tables should upgrade immediately.
