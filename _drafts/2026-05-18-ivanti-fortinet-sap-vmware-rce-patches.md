---
title: "Critical Patches: Ivanti CVSS 9.6 RCE, Plus Fortinet, SAP, VMware, n8n Fixes"
date: 2026-05-18 10:54:00 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, sqli, privilege-escalation, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html
---

Five enterprise vendors released security patches in a coordinated disclosure. The most critical is CVE-2026-8043 in Ivanti Xtraction (CVSS 9.6), enabling information disclosure and client-side attacks via external file name control. Fortinet, SAP, VMware, and workflow automation platform n8n also issued fixes addressing authentication bypass, SQL injection, remote code execution, and privilege escalation vulnerabilities. Organizations should prioritize patching Ivanti Xtraction given its near-perfect CVSS score, followed by Fortinet and VMware given their broad enterprise deployment. n8n deployments exposed to the internet or integrated into agentic AI workflows warrant immediate attention.
