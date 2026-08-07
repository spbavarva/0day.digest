---
title: "Automate Certificates With ACME Support in AWS Certificate Manager"
date: 2026-08-06 22:03:36 +0000
categories: [Daily Signal]
tags: [aws, cloud-security]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/automate-certificates-with-acme-support-in-aws-certificate-manager/
---

AWS Certificate Manager now supports the ACME protocol for automated issuance
and renewal of TLS certificates. The launch is timed to a CA/Browser Forum
mandate phasing down maximum public certificate validity: 100 days by March
2027, then 47 days by March 2029. Manual rotation becomes impractical at those
intervals, making automation close to a requirement for compliance. Teams
managing TLS at scale on AWS should evaluate migrating cert issuance workflows
to ACME-based automation ahead of the 2027 deadline.
