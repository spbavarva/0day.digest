---
title: "Datasette Apps Lets You Run Sandboxed HTML Apps Against Your Data"
date: 2026-06-18 23:58:38 +0000
categories: [Daily Signal]
tags: [appsec, llm]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything
---

Simon Willison's Datasette project launched "Datasette Apps," a plugin that
hosts self-contained HTML+JavaScript applications inside a constrained
iframe sandbox on a Datasette instance. These apps can run read-only SQL
queries against the underlying data by default, and write queries only if
explicitly configured with stored queries. The sandboxing model is notable
because it lets users embed untrusted or AI-generated frontend code while
limiting its access to the database layer. It's a practical pattern for
safely exposing LLM-generated UI code against real data without granting
full database access.
