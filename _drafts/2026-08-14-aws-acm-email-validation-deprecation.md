---
title: "AWS Certificate Manager Will Discontinue Email Validation for Public Certificates"
date: 2026-08-14 21:23:00 +0000
categories: [Daily Signal]
tags: [aws, cloud-security]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/aws-certificate-manager-will-discontinue-email-validation-to-prove-domain-validation-for-certificates/
---

AWS Certificate Manager will discontinue support for email-validated public
certificates by September 30, 2027. The change follows the CA/Browser
Forum's industry-wide deprecation of email-based domain validation.

Teams still using email validation for ACM public certificates need to
migrate to DNS validation before the deadline to avoid certificate issuance
or renewal failures.
