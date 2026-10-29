---
title: "26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories"
date: 2026-10-29 11:33:15 +0000
categories: [Daily Signal]
tags: [data-breach, iam, cloud-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/26400-valid-cloud-and-ai-credentials.html
---

Independent researcher Ben Zimmermann scanned 7.25 million public
repositories on Gitee, a Chinese code-hosting service, and found 26,400
credentials that still worked.

Most were keys for cloud and AI services that developers had left in
public code. Anyone who copied one of the credentials could have used it.
The results were reported on October 28. Teams using Gitee should audit
repos for committed secrets and rotate any exposed keys.
