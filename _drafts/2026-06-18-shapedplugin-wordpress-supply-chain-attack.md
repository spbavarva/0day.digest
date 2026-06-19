---
title: "ShapedPlugin Update Mechanism Hijacked to Distribute Malware to WordPress Sites"
date: 2026-06-18 12:55:36 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/
---

Multiple WordPress plugins from vendor ShapedPlugin were compromised in a
supply chain attack that pushed infected releases to paying customers
through the vendor's official update system. Because the malicious code
was distributed via a trusted, legitimate update channel, affected sites
could have been infected through normal automatic updates with no other
action required. WordPress site operators using ShapedPlugin products
should treat recent updates as untrusted, verify file integrity against
known-good releases, and rotate credentials on affected sites.
