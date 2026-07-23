---
title: "PyPI Blocks Uploads to Releases Older Than 14 Days to Curb Supply Chain Poisoning"
date: 2026-07-23 04:50:36 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi]
severity: informational
must_know: false
sources:
  - name: Simon Willison (quoting Seth Larson, PyPI blog)
    url: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
---

PyPI now rejects new file uploads to releases older than 14 days. The
change, described by PyPI's Seth Larson, closes a window where a
compromised publishing token or CI workflow could be used to silently
poison a long-stable, trusted package release. Larson notes there's no
confirmed case of this attack vector being abused yet — the restriction is
preventive, closing a gap that simply hadn't been exploited before now.
