---
title: "Twin Path Traversal CVEs Found in Kubernetes CSI Storage Drivers"
date: 2026-07-23 13:00:50 +0000
categories: [Daily Signal]
tags: [kubernetes, container-security, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: SentinelOne Labs
    url: https://www.sentinelone.com/blog/mount-here-read-there-twin-path-traversal-cves-in-kubernetes-storage/
---

SentinelOne Labs disclosed two path traversal vulnerabilities in Kubernetes
CSI (Container Storage Interface) drivers, caused by a common misconception
around how Go's filepath.Join function sanitizes input. The flaws allow
cross-tenant path traversal, letting a workload in one tenant potentially
read data belonging to another via the storage layer. No CVE identifiers or
patch status were included in the available summary. Clusters using
affected CSI drivers should review SentinelOne's advisory for mitigation
guidance.
