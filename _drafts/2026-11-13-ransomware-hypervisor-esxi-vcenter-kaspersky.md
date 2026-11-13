---
title: "Ransomware at the Hypervisor Layer: ESXi and vCenter Abuse Techniques"
date: 2026-11-13 09:00:43 +0000
categories: [Daily Signal]
tags: [ransomware]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/esxi-ransomware/121959/
---

Kaspersky's GReAT team analyzed a ransomware incident that operated at the
hypervisor layer, abusing built-in ESXi and vCenter features for malicious
purposes. The write-up explains why hypervisors remain difficult to monitor
and outlines common access paths adversaries use to reach them.

Organizations running VMware ESXi/vCenter should review hypervisor-layer
logging and access controls, which typically receive less monitoring
attention than guest VMs.
