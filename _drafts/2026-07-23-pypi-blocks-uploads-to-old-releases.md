---
title: "PyPI Now Rejects Uploads to Releases Older Than 14 Days"
date: 2026-07-23 04:50:36 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
---

The Python Package Index now rejects new file uploads to releases older
than 14 days, according to PyPI's Seth Larson as quoted by Simon Willison.
The restriction is meant to prevent old, long-stable releases from being
poisoned if a project's publishing tokens or CI workflows are later
compromised. PyPI says it isn't aware of this technique being abused yet,
but there was no technical barrier preventing it before the change. The
move tightens the supply-chain security posture for the Python packaging
ecosystem.
