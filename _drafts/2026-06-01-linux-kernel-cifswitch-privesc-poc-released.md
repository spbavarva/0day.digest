---
title: "19-Year-Old Linux Kernel CIFSwitch Vulnerability Gets Public PoC — Local Privilege Escalation to Root"
date: 2026-06-01 11:19:31 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/19-year-old-linux-kernel-vulnerability-exposes-systems-to-root-access/
---

A privilege escalation vulnerability in the Linux kernel's CIFSwitch component has been present for 19 years and now has a published proof-of-concept exploit that allows low-privileged local users to escalate to root on vulnerable systems. The flaw's age means it is present across a broad range of kernel versions and Linux distributions.

Distribution vendors are expected to release patches. Systems most at risk are those with untrusted local users: shared hosting environments, multi-tenant container hosts, and systems with uncontrolled user namespace access. Monitor distribution security advisories for patch availability.
