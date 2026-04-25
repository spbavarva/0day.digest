---
title: "AWS Publishes Post-Quantum Cryptography Migration Guide: Addressing Harvest Now, Decrypt Later"
date: 2026-04-24 18:53:00 +0000
categories: [Daily Signal]
tags: [cloud-security, aws, cryptography]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/protecting-your-secrets-from-tomorrows-quantum-risks/
---

AWS has released technical guidance on migrating workloads to post-quantum cryptography (PQC) as
part of its broader PQC migration plan. The post focuses on the harvest now, decrypt later (HNDL)
threat model, where adversaries collect encrypted traffic today intending to decrypt it once quantum
computers become viable.

The guidance covers client-side migration steps within the AWS shared responsibility model. Key
actions include upgrading TLS and key exchange to NIST-standardized PQC algorithms (ML-KEM, ML-DSA)
for workloads handling sensitive long-lived data. Organizations in regulated industries or with
long data-retention requirements (finance, healthcare, government) should prioritize this migration
now, as HNDL-collected data may be decryptable within the planning horizons of current threat actors.
