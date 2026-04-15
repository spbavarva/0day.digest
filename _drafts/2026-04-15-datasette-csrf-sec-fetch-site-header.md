---
title: "Datasette Drops CSRF Tokens in Favor of Sec-Fetch-Site Header Protection"
date: 2026-04-15 00:00:00 +0000
categories: [Daily Signal]
tags: [appsec]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Apr/14/replace-token-based-csrf/#atom-everything
---

Simon Willison has merged a PR in Datasette that replaces traditional CSRF token protection
with Sec-Fetch-Site header validation, following research by Filippo Valsorda. The Sec-Fetch-Site
header is a browser-native metadata header that indicates whether a request originates from
the same site, a cross-site origin, or direct navigation.

The practical advantage: no more hidden CSRF token fields scattered across templates, no
server-side token state to manage, and no friction for programmatic API callers. The tradeoff
is reliance on browsers sending the header correctly — a safe assumption for modern browsers
but potentially unreliable for older or non-standard clients.

This is a meaningful technique evolution worth evaluating for other web frameworks. The approach
works well for applications where all legitimate cross-origin requests are intended to be API
calls rather than form submissions, and where the user base is expected to use modern browsers.
