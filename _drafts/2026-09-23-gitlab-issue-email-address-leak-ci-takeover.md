---
title: "Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You"
date: 2026-09-23 16:53:10 +0000
categories: [Daily Signal]
tags: [appsec, privilege-escalation, devsecops]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
---

GitLab gives each user a private email address for filing issues by
email, exposed behind a button labeled "Email work item to this
project." Anyone who obtains that address can email GitLab a patch
that gets committed in the victim's name to any branch they can push
to, including main, and can trigger CI/CD jobs that run as that user.

Because the address functions as a bearer credential, its exposure
via logs, headers, or accidental disclosure is enough to grant an
attacker code-push and CI-execution capability under someone else's
identity. GitLab users should treat the address as sensitive.
