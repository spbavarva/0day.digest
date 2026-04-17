---
title: "Payouts King Ransomware Deploys QEMU VMs to Evade Endpoint Security"
date: 2026-04-17 19:10:00 +0000
categories: [Daily Signal]
tags: [ransomware, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/payouts-king-ransomware-uses-qemu-vms-to-bypass-endpoint-security/
---

The Payouts King ransomware group is deploying the QEMU open-source hypervisor on compromised
systems to spin up hidden virtual machines, then using those VMs to establish reverse SSH backdoors
to attacker infrastructure.

By running malicious activity inside a legitimate QEMU guest, the technique sidesteps signature-based
endpoint detection tools that cannot inspect processes or network traffic originating inside the guest
environment. QEMU's status as a legitimate enterprise virtualization tool makes it easy to allowlist
and difficult to block without broader operational impact.

Security teams should hunt for unexpected QEMU processes in their environments, particularly on
systems where virtualization has no legitimate business purpose. Monitor outbound SSH sessions from
hosts where QEMU is not expected, and consider restricting QEMU installation via application control
policies in environments where it is not required.
